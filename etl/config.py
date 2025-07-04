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
                {"name": "MUNICIPIO", "type": "string", "size":"8", "clean":True},
                {"name": "COD_DANE", "type": "numeric", "size":"12", "clean":True},
                {"name": "ESTABLECIMIENTO", "type": "string" , "size":"40", "clean":True},
                {"name": "TIPO_ESTABLECIMIENTO", "type": "string" , "size":"30", "clean":True},
                {"name": "SECTOR", "type": "string" , "size":"10", "clean":True},
                {"name": "DANE_SEDE", "type": "numeric" , "size":"12", "clean":True},
                {"name": "CONS_SEDE", "type": "numeric" , "size":"15", "clean":True},
                {"name": "NOMBRE_SEDES", "type": "string" , "size":"10", "clean":True},
                {"name": "ZONAS", "type": "string" , "size":"10", "clean":True},
                {"name": "COD_TIPO_DOC", "type": "numeric" , "size":"2","encrypt": True ,"clean":True},
                {"name": "TIPO_DOC", "type": "string" , "size":"4", "clean":True},
                {"name": "NRO_IDENTIDAD", "type": "numeric" , "size":"12", "clean":True, "encrypt": True},
                {"name": "COD_DEPTO_EXPIDE", "type": "numeric" , "size":"2", "clean":True},
                {"name": "COD_MPIO_EXPIDE", "type": "string" , "size":"3", "clean":True},
                {"name": "PRI_APE", "type": "string" , "size":"12", "clean":True},
                {"name": "SEG_APE", "type": "string" , "size":"12", "clean":True},
                {"name": "PRI_NOM", "type": "string" , "size":"12", "clean":True},
                {"name": "SEG_NOM", "type": "string" , "size":"12", "clean":True},
                {"name": "CONCATENAR", "type": "string" , "size":"40", "clean":True},
                {"name": "DIRECCION_RESIDENCIA", "type": "string" , "size":"10", "clean":True, "encrypt": True},
                {"name": "TELEFONO", "type": "numeric" , "size":"10", "clean":True},
                {"name": "COD_DPTO_RESIDE", "type": "numeric" , "size":"2", "clean":True, "encrypt": True},
                {"name": "COD_MPIO_RESIDE", "type": "numeric" , "size":"3", "clean":True, "encrypt": True},
                {"name": "ESTRATO", "type": "numeric" , "size":"1", "clean":True},
                {"name": "SISBEN", "type": "string" , "size":"10", "clean":True},
                {"name": "FECHA_NACIMIENTO", "type": "numeric" , "size":"10", "clean":True, "encrypt": True},
                {"name": "EDAD_ANIOS", "type": "numeric", "size":"2", "clean":True},
                {"name": "EDAD", "type": "numeric" , "size":"2", "clean":True, "encrypt": True},
                {"name": "COD_DPTO_NAC", "type": "numeric"  , "size":"2", "clean":True},
                {"name": "COD_MPIO_NAC", "type": "string" , "size":"3", "clean":True},
                {"name": "GENERO", "type": "string" , "size":"1", "clean":True, "encrypt": True},
                {"name": "POB_VICT_CONF", "type": "string" , "size":"2", "clean":True},
                {"name": "PROV_SEC_PRIV", "type": "string" , "size":"2", "clean":True},
                {"name": "PROV_OTRO_MUNICIPIO", "type": "string" , "size":"2", "clean":True},
                {"name": "COD_TIPO_DISCA", "type": "numeric" , "size":"2", "clean":True},
                {"name": "TIPOS_DISCAPACIDAD", "type": "string" , "size":"12", "clean":True},
                {"name": "COD_CAP_EXCEP", "type": "numeric" , "size":"2", "clean":True},
                {"name": "CAPACIDADES_EXCEPCIONALES", "type": "string" , "size":"12", "clean":True},
                {"name": "COD_ETNIA", "type": "string" , "size":"2", "clean":True},
                {"name": "ETNIA", "type": "string" , "size":"20", "clean":True},
                {"name": "ETNIA_1", "type": "string" , "size":"12", "clean":True},
                {"name": "COD_RESGUARDO", "type": "string" , "size":"3", "clean":True, "encrypt": True},
                {"name": "RESGUARDO", "type": "string" , "size":"12", "clean":True},
                {"name": "INSTITUCION_BIENESTAR_ORIGEN", "type": "string" , "size":"12", "clean":True},
                {"name": "COD_JOR", "type": "numeric" , "size":"2", "clean":True},
                {"name": "JORNADA", "type": "numeric" , "size":"10", "clean":True},
                {"name": "COD_CARACTER", "type": "string" , "size":"2", "clean":True},
                {"name": "CARACTER", "type": "string" , "size":"10", "clean":True},
                {"name": "COD_ESP", "type": "string" , "size":"3", "clean":True},
                {"name": "ESPECIALIDADES", "type": "string" , "size":"10", "clean":True},
                {"name": "COD_GRADO", "type": "string" , "size":"2", "clean":True},
                {"name": "GRADO", "type": "string" , "size":"10", "clean":True},
                {"name": "COD_GRUPO", "type": "numeric" , "size":"4", "clean":True},
                {"name": "COD_MET", "type": "numeric" , "size":"2", "clean":True},
                {"name": "METODOLOGIAS", "type": "string" , "size":"14", "clean":True},
                {"name": "MATRICULA_CONTRATADA", "type": "string" , "size":"2", "clean":True},
                {"name": "REPITENTE", "type": "string" , "size":"2", "clean":True},
                {"name": "NUEVO", "type": "string" , "size":"2", "clean":True},
                {"name": "COD_FTE_REC", "type": "numeric" , "size":"2", "clean":True},
                {"name": "FUENTE_RECURSO", "type": "string" , "size":"3", "clean":True},
                {"name": "COD_ZONA_ALU", "type": "numeric" , "size":"2", "clean":True},
                {"name": "ZONA_RESIDE_ALUMNO", "type": "string" , "size":"8", "clean":True},
                {"name": "CAB_FAMILIA", "type": "string" , "size":"2", "clean":True},
                {"name": "BEN_MAD_FLIA", "type": "string" , "size":"2", "clean":True},
                {"name": "BEN_VET_FP", "type": "string"  , "size":"2", "clean":True},
                {"name": "BEN_HER_NAC", "type": "string" , "size":"2", "clean":True},
                {"name": "CODIGO_INTERNADO", "type": "numeric" , "size":"2", "clean":True},
                {"name": "INTERNADO", "type": "string" , "size":"2", "clean":True},
                {"name": "CODIGO_VALORACION_1", "type": "string" , "size":"2", "clean":True},
                {"name": "CODIGO_VALORACION_2", "type": "string" , "size":"2", "clean":True},
                {"name": "NUM_CONVENIO", "type": "string" , "size":"2", "clean":True},
                {"name": "PER_ID", "type": "numeric" , "size":"10", "clean":True},
                {"name": "FEC_CORTE", "type": "numeric" , "size":"9", "clean":True},
                {"name": "NIVEL", "type": "string" , "size":"14", "clean":True},
                {"name": "CALENDARIO", "type": "string" , "size":"1", "clean":True},
                {"name": "PRESTADOR 2022", "type": "string" , "size":"10", "clean":True},
                {"name": "NUMERO CONTRATO", "type": "string" , "size":"10", "clean":True},
                {"name": "POBLACION", "type": "string" , "size":"14", "clean":True},
                {"name": "Región", "type": "string" , "size":"6", "clean":True},
                {"name": "carácter", "type": "string" , "size":"12", "clean":True},
                {"name": "APOYO_ACADEMICO_ESPECIAL", "type": "stringc" , "size":"2", "clean":True},
                {"name": "SRPA", "type": "string" , "size":"2", "clean":True},
                {"name": "PAIS_ORIGEN", "type": "numeric" , "size":"3", "clean":True},
                {"name": "NACIONALIDAD", "type": "string" , "size":"10", "clean":True},
                {"name": "TRASTORNOS_ESPECIFICOS", "type": "string" , "size":"2", "clean":True},
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

