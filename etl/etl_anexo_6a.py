import pandas as pd
import os

def procesar_anexo_6a(nombre_archivo, fecha_corte):
    """
    Lee el archivo Anexo_6A, agrega la columna de fecha de corte,
    y guarda el resultado en data/processed/.
    """
    ruta_entrada = os.path.join('data', 'raw', nombre_archivo)
    ruta_salida = os.path.join('data', 'processed', f'procesado_{nombre_archivo}')
    
    # Leer el archivo CSV
    df = pd.read_csv(ruta_entrada, dtype=str)
        
    # Agregar columna de fecha de corte
    df['fecha_corte'] = fecha_corte
    
    # Guardar el archivo procesado
    df.to_csv(ruta_salida, index=False)
    print(f"Archivo procesado guardado en: {ruta_salida}")

# Ejemplo de uso:
# procesar_anexo_6a('Anexo_6A_20250620_Lote1.csv', '2025-06-20')