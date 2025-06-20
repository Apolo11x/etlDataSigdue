# Script principal para ejecutar el ETL
import os
from etl.etl_anexo_6a import procesar_anexo_6a
from datetime import datetime   

def main():
    # Definir el nombre del archivo y la fecha de corte
    nombre_archivo = "./data/raw/ANEXO_6A_CORTE_01062025.csv"  # Reemplaza con el nombre real del archivo
    fecha_corte = datetime.strptime('01062025', '%d%m%Y').date()
    # Definir el nombre del archivo y la fecha de corte
    nombre_archivo = "nombre_del_archivo.csv"  # Reemplaza con el nombre real del archivo
    ruta_archivo = os.path.join('data', 'raw', nombre_archivo)
    
    # Procesar el Anexo 6A
    procesar_anexo_6a(nombre_archivo, fecha_corte)