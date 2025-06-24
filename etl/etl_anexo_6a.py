import pandas as pd
import os
import unicodedata
import re
import logging
from datetime import datetime

# Configuración del logger
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f"etl_anexo_6a_{datetime.now().strftime('%Y%m%d')}.log")
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

def procesar_anexo_6a(nombre_archivo, fecha_corte, separador=';'):
    """
    Lee el archivo CSV desde data/raw, agrega la columna de fecha de corte,
    y guarda el resultado en data/processed/ con el nombre de archivo
    precedido por la fecha de corte.
    """
    ruta_entrada = os.path.join('data', 'raw', nombre_archivo)
    nuevo_nombre = f"{fecha_corte}_{nombre_archivo}"
    ruta_salida = os.path.join('data', 'processed', nuevo_nombre)
    
    try:
        df = pd.read_csv(ruta_entrada, dtype=str, sep=separador)
    except Exception as e:
        logging.error(f"Error al leer el archivo CSV en la línea de lectura: {e}")
        raise
        
    df['fecha_corte'] = fecha_corte
    
    def limpiar_texto(texto):
        try:
            if pd.isna(texto):
                return texto
            # Quitar tildes y apostrofes
            texto = unicodedata.normalize('NFKD', str(texto)).encode('ASCII', 'ignore').decode('utf-8')
            # Quitar comas y reemplazar por espacio
            texto = texto.replace(',', ' ')
            # Quitar comillas simples y dobles
            texto = texto.replace("'", '').replace('"', '')
            return texto
        except Exception as e:
            logging.error(f"Error en limpiar_texto con valor '{texto}': {e} (línea: texto = unicodedata.normalize...)")
            return texto

    for col in df.columns:
        if df[col].dtype == object:
            df[col] = df[col].apply(limpiar_texto)

    for col in df.columns:
        if 'fecha' in col.lower():
            try:
                df[col] = pd.to_datetime(df[col], errors='coerce').dt.strftime('%d/%m/%Y')
            except Exception as e:
                logging.warning(f"No se pudo transformar la columna '{col}' a formato fecha: {e} (línea: pd.to_datetime...)")
    
    try:
        df.to_csv(ruta_salida, index=False, sep=';')
        logging.info(f"Archivo procesado guardado en: {ruta_salida}")
    except Exception as e:
        logging.error(f"Error al guardar el archivo procesado: {e} (línea: df.to_csv...)")
        raise
    print(f"Archivo procesado guardado en: {ruta_salida}")

# Ejemplo de uso:
# procesar_anexo_6a('Anexo_6A_20250620_Lote1.csv', '2025-06-20')