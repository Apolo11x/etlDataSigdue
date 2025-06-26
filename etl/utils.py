# Funciones auxiliares
import pandas as pd
import os
import unicodedata
import re
import logging
from datetime import datetime

# Configuración del logger
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f"ANEXO_6A.csv{datetime.now().strftime('%Y%m%d')}.log")
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

def estandarizar_archivo(nombre_archivo, fecha_proceso=None, separador=';'):
    ruta_entrada = os.path.join('data', 'raw', nombre_archivo)
    if fecha_proceso is None:
        fecha_proceso = datetime.now().strftime('%Y-%m-%d')
    nuevo_nombre = f"{fecha_proceso}_{nombre_archivo}"
    ruta_salida = os.path.join('data', 'processed', nuevo_nombre)

    try:
        # Prueba primero con utf-8, si ves caracteres raros, cambia a latin1
        df = pd.read_csv(ruta_entrada, dtype=str, sep=',', encoding='utf-8')
    except Exception as e:
        logging.error(f"Error al leer el archivo CSV: {e}")
        raise

    # Limpiar encabezados
    df.columns = [unicodedata.normalize('NFKD', str(col)).encode('ASCII', 'ignore').decode('utf-8').replace("'", '').replace('"', '') for col in df.columns]

    df['fecha_proceso'] = fecha_proceso

    def limpiar_texto(texto):
        try:
            if pd.isna(texto):
                return texto
            texto = unicodedata.normalize('NFKD', str(texto)).encode('ASCII', 'ignore').decode('utf-8')
            texto = texto.replace(',', ' ')
            texto = texto.replace("'", '').replace('"', '')
            return texto
        except Exception as e:
            logging.error(f"Error en limpiar_texto con valor '{texto}': {e}")
            return texto

    # Limpiar todos los valores
    for col in df.columns:
        df[col] = df[col].apply(lambda x: limpiar_texto(str(x)) if pd.notna(x) else x)

    # Normalizar fechas
    for col in df.columns:
        if 'fecha' in col.lower():
            try:
                df[col] = pd.to_datetime(df[col], errors='coerce').dt.strftime('%d/%m/%Y')
            except Exception as e:
                logging.warning(f"No se pudo transformar la columna '{col}' a formato fecha: {e}")

    try:
        df.to_csv(ruta_salida, index=False, sep=';')
        logging.info(f"Archivo procesado guardado en: {ruta_salida}")
    except Exception as e:
        logging.error(f"Error al guardar el archivo procesado: {e}")
        raise
    print(f"Archivo procesado guardado en: {ruta_salida}")

    # ...al final del archivo, sin sangría
if __name__ == "__main__":
    estandarizar_archivo('ANEXO_6A.csv', separador=',')
