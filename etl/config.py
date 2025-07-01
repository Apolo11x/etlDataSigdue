# Configuración del proyecto
import os
import json
import pandas as pd
# Ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Rutas de carpetas principales
DATA_RAW_DIR = os.path.join(BASE_DIR, 'data', 'raw')
DATA_PROCESSED_DIR = os.path.join(BASE_DIR, 'data', 'processed')
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
SCHEMAS_DIR = os.path.join(BASE_DIR, 'schemas')

# Ejemplo de uso para construir la ruta de un archivo específico
def get_raw_file_path(filename):
    return os.path.join(DATA_RAW_DIR, filename)

def get_processed_file_path(filename):
    return os.path.join(DATA_PROCESSED_DIR, filename)


# ...existing code...

def get_initial_config(file_type="archivo_sigdue.csv"):
    """
    Retorna una configuración inicial en formato JSON para el tipo de archivo especificado.
    """
    configs = {
        "csv": {
            "delimiter": ",",
            "encoding": "utf-8",
            "has_header": True,
            "fields": [
#                {"name": "Nombre del Campo", 
#                 "type": "Tipo del Campo", 
#                 "size":"Tamaño", 
#                 "clean":True #limpiar? , 
#                 "encrypt": True # Cifrar ? , 
#                 "load": True # Cargar en la base de datos , 
#                 "field": "ANO"
# },
                {"name": "AÑO", "type": "numeric", "size":"4", "clean":True},
                {"name": "COD_MPIO", "type": "numeric", "size":"3", "clean":True},
                {"name": "MUNICIPIO", "type": "string"},
                {"name": "COD_DANE", "type": "numeric"},
                {"name": "ESTABLECIMIENTO", "type": "string"},
                {"name": "TIPO_ESTABLECIMIENTO", "type": "string"},
                {"name": "SECTOR", "type": "string"},
                {"name": "DANE_SEDE", "type": "numeric"},
                {"name": "CONS_SEDE", "type": "string"},
                {"name": "NOMBRE_SEDES", "type": "string"},
                {"name": "ZONAS", "type": "string"},
                {"name": "COD_TIPO_DOC", "type": "numeric"},
                {"name": "TIPO_DOC", "type": "numeric"},
                {"name": "NRO_IDENTIDAD", "type": "numeric"},
                {"name": "COD_DEPTO_EXPIDE", "type": "numeric"},
                {"name": "COD_MPIO_EXPIDE", "type": "numeric"},
                {"name": "PRI_APE", "type": "string"},
                {"name": "SEG_APE", "type": "string"},
                {"name": "PRI_NOM", "type": "string"},
                {"name": "SEG_NOM", "type": "string"},
                {"name": "CONCATENAR", "type": "string"},
                {"name": "DIRECCION_RESIDENCIA", "type": "string"},
                {"name": "TELEFONO", "type": "numeric"},
                {"name": "COD_DPTO_RESIDE", "type": "numeric"},
                {"name": "COD_MPIO_RESIDE", "type": "numeric"},
                {"name": "ESTRATO", "type": "numeric"},
                {"name": "SISBEN", "type": "string"},
                {"name": "FECHA_NACIMIENTO", "type": "string"},
                {"name": "EDAD_ANIOS", "type": "numeric"},
                {"name": "EDAD", "type": "numeric"},
                {"name": "COD_DPTO_NAC", "type": "numeric"},
                {"name": "COD_MPIO_NAC", "type": "numeric"},
                {"name": "GENERO", "type": "string"},
                {"name": "POB_VICT_CONF", "type": "string"},
                {"name": "PROV_SEC_PRIV", "type": "string"},
                {"name": "PROV_OTRO_MUNICIPIO", "type": "string"},
                {"name": "COD_TIPO_DISCA", "type": "numeric"},
                {"name": "TIPOS_DISCAPACIDAD", "type": "string"},
                {"name": "COD_CAP_EXCEP", "type": "numeric"},
                {"name": "CAPACIDADES_EXCEPCIONALES", "type": "string"},
                {"name": "COD_ETNIA", "type": "numeric"},
                {"name": "ETNIA", "type": "string"},
                {"name": "ETNIA_1", "type": "string"},
                {"name": "COD_RESGUARDO", "type": "numeric"},
                {"name": "RESGUARDO", "type": "string"},
                {"name": "INSTITUCION_BIENESTAR_ORIGEN", "type": "string"},
                {"name": "COD_JOR", "type": "numeric"},
                {"name": "JORNADA", "type": "numeric"},
                {"name": "COD_CARACTER", "type": "numeric"},
                {"name": "CARACTER", "type": "string"},
                {"name": "COD_ESP", "type": "string"},
                {"name": "ESPECIALIDADES", "type": "string"},
                {"name": "COD_GRADO", "type": "numeric"},
                {"name": "GRADO", "type": "string"},
                {"name": "COD_GRUPO", "type": "numeric"},
                {"name": "COD_MET", "type": "numeric"},
                {"name": "METODOLOGIAS", "type": "string"},
                {"name": "MATRICULA_CONTRATADA", "type": "string"},
                {"name": "REPITENTE", "type": "string"},
                {"name": "NUEVO", "type": "string"},
                {"name": "COD_FTE_REC", "type": "numeric"},
                {"name": "FUENTE_RECURSO", "type": "string"},
                {"name": "COD_ZONA_ALU", "type": "numeric"},
                {"name": "ZONA_RESIDE_ALUMNO", "type": "string"},
                {"name": "CAB_FAMILIA", "type": "string"},
                {"name": "BEN_MAD_FLIA", "type": "string"},
                {"name": "BEN_VET_FP", "type": "string"},
                {"name": "BEN_HER_NAC", "type": "string"},
                {"name": "CODIGO_INTERNADO", "type": "numeric"},
                {"name": "INTERNADO", "type": "string"},
                {"name": "CODIGO_VALORACION_1", "type": "numeric"},
                {"name": "CODIGO_VALORACION_2", "type": "nuemeric"},
                {"name": "NUM_CONVENIO", "type": "numeric"},
                {"name": "PER_ID", "type": "numeric"},
                {"name": "FEC_CORTE", "type": "numeric"},
                {"name": "NIVEL", "type": "string"},
                {"name": "CALENDARIO", "type": "string"},
                {"name": "PRESTADOR 2022", "type": "string"},
                {"name": "NUMERO CONTRATO", "type": "string"},
                {"name": "POBLACION", "type": "string"},
                {"name": "Región", "type": "string"},
                {"name": "carácter", "type": "string"},
                {"name": "APOYO_ACADEMICO_ESPECIAL", "type": "numeric"},
                {"name": "SRPA", "type": "numeric"},
                {"name": "PAIS_ORIGEN", "type": "numeric"},
                {"name": "NACIONALIDAD", "type": "string"},
                {"name": "TRASTORNOS_ESPECIFICOS", "type": "string"}
            ]
        }
    }
    config = configs.get(file_type.lower())
    if config is None:
        raise ValueError(f"Tipo de archivo no soportado: {file_type}")
    return json.dumps(config, indent=4, ensure_ascii=False)
# ...existing code...


if __name__ == "__main__":
    print(get_initial_config("csv"))

