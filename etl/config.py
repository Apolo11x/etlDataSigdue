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
#                {"name": "Nombre del Campo", ##NOMBRE DEL CAMPO DEL DE CSV
#                 "type": "Tipo del Campo", DE LA BASE DE DATOS
#                 "size":"Tamaño", 
#                 "clean":True #limpiar? , 
#                 "encrypt": True # Cifrar ? , 
#                 "load": True # Cargar en la base de datos , 
#                 "field": "ANO" CAMPO DONDE VA A SER ALAMCENADO
# },
                {"name": "ANO", "type": "string", "size":"4", "clean":True, "load": True, "field": "ANO"},
                {"name": "COD_MPIO", "type": "string", "size":"3", "clean":True, "load": True, "field": "COD_MPIO"},
                {"name": "MUNICIPIO", "type": "string", "size":"8", "clean":True, "load": True, "field": "MUNICIPIO"},
                {"name": "COD_DANE", "type": "string", "size":"12", "clean":True , "load": True, "field": "COD_DANE"},
                {"name": "ESTABLECIMIENTO", "type": "string" , "size":"40", "clean":True, "load": True, "field": "ESTABLECIMIENTO"},
                {"name": "TIPO_ESTABLECIMIENTO", "type": "string" , "size":"30", "clean":True, "load": True, "field": "TIPO_ESTABLECIMIENTO"},
                {"name": "SECTOR", "type": "string" , "size":"10", "clean":True, "load": True, "field": "SECTOR"},
                {"name": "DANE_SEDE", "type": "string" , "size":"12", "clean":True, "load": True, "field": "DANE_SEDE"},
                {"name": "CONS_SEDE", "type": "string" , "size":"15", "clean":True , "load": True, "field": "CONS_SEDE"},
                {"name": "NOMBRE_SEDES", "type": "string" , "size":"10", "clean":True, "load": True, "field": "NOMBRE_SEDES"},
                {"name": "ZONAS", "type": "string" , "size":"10", "clean":True, "load": True, "field": "ZONAS"},
                {"name": "COD_TIPO_DOC", "type": "string" , "size":"2","clean":True, "load": True, "field": "COD_TIPO_DOC"},
                {"name": "TIPO_DOC", "type": "string" , "size":"4", "clean":True, "load": True, "field": "TIPO_DOC"},
                {"name": "NRO_IDENTIDAD", "type": "string" , "size":"12", "clean":True, "encrypt": True , "load": True, "field": "NRO_IDENTIDAD"},
                {"name": "COD_DEPTO_EXPIDE", "type": "string" , "size":"2", "clean":True ,"load": True, "field": "COD_DEPTO_EXPIDE"},
                {"name": "COD_MPIO_EXPIDE", "type": "string" , "size":"3", "clean":True, "load": True, "field": "COD_MPIO_EXPIDE"},
                {"name": "PRI_APE", "type": "string" , "size":"20", "clean":True, "load": True, "field": "PRI_APE, "},
                {"name": "SEG_APE", "type": "string" , "size":"20", "clean":True, "load": True, "field": "SEG_APE"},
                {"name": "PRI_NOM", "type": "string" , "size":"20", "clean":True, "load": True, "field": "PRI_NOM"},
                {"name": "SEG_NOM", "type": "string" , "size":"20", "clean":True, "load": True, "field": "SEG_NOM"},
                {"name": "CONCATENAR", "type": "string" , "size":"40", "clean":True, "load": True, "field": "CONCATENAR"},
                {"name": "DIRECCION_RESIDENCIA", "string": "string" , "size":"10", "clean":True, "encrypt": True, "load": True, "field": "DIRECCION_RESIDENCIA"},
                {"name": "TELEFONO", "type": "string" , "size":"10", "clean":True, "load": True, "field": "TELEFONO"},
                {"name": "COD_DPTO_RESIDE", "type": "string" , "size":"2", "clean":True, "load": True, "field": "COD_DPTO_RESIDE"},
                {"name": "COD_MPIO_RESIDE", "type": "string" , "size":"3", "clean":True, "load": True, "field": "COD_MPIO_RESIDE"},
                {"name": "ESTRATO", "type": "string" , "size":"1", "clean":True , "load": True, "field": "ESTRATO"},
                {"name": "SISBEN", "type": "string" , "size":"10", "clean":True, "load": True, "field": "SISBEN"},
                {"name": "FECHA_NACIMIENTO", "type": "string" , "size":"10", "clean":True, "encrypt": True, "load": True, "field": "FECHA_NACIMIENTO"},
                {"name": "EDAD_ANIOS", "type": "string", "size":"2", "clean":True, "load": True, "field": "EDAD_ANIOS"},
                {"name": "EDAD", "type": "string" , "size":"2", "clean":True, "encrypt": True, "load": True, "field": "EDAD"},
                {"name": "COD_DPTO_NAC", "type": "string"  , "size":"2", "clean":True, "load": True, "field": "COD_DPTO_NAC"},
                {"name": "COD_MPIO_NAC", "type": "string" , "size":"3", "clean":True, "load": True, "field": "COD_MPIO_NAC"},
                {"name": "GENERO", "type": "string" , "size":"1", "clean":True,  "load": True, "field": "GENERO"},
                {"name": "POB_VICT_CONF", "type": "string" , "size":"2", "clean":True , "load": True, "field": "POB_VICT_CONF"},
                {"name": "PROV_SEC_PRIV", "type": "string" , "size":"2", "clean":True, "load": True, "field": "PROV_SEC_PRIV"},
                {"name": "PROV_OTRO_MUNICIPIO", "type": "string" , "size":"2", "clean":True, "load": True, "field": "PROV_OTRO_MUNICIPIO"},
                {"name": "COD_TIPO_DISCA", "type": "string" , "size":"2", "clean":True, "load": True, "field": "COD_TIPO_DISCA"},
                {"name": "TIPOS_DISCAPACIDAD", "type": "string" , "size":"12", "clean":True, "load": True, "field": "TIPOS_DISCAPACIDAD"},
                {"name": "COD_CAP_EXCEP", "type": "string" , "size":"2", "clean":True, "load": True, "field": "COD_CAP_EXCEP"},
                {"name": "CAPACIDADES_EXCEPCIONALES", "type": "string" , "size":"12", "clean":True, "load": True, "field": "CAPACIDADES_EXCEPCIONALES"},
                {"name": "COD_ETNIA", "type": "string" , "size":"2", "clean":True, "load": True, "field": "COD_ETNIA"},
                {"name": "ETNIA", "type": "string" , "size":"20", "clean":True, "load": True, "field": "ETNIA"},
                {"name": "ETNIA_1", "type": "string" , "size":"12", "clean":True, "load": True, "field": "ETNIA_1"},
                {"name": "COD_RESGUARDO", "type": "string" , "size":"3", "clean":True, "encrypt": True, "load": True, "field": "COD_RESGUARDO"},
                {"name": "RESGUARDO", "type": "string" , "size":"12", "clean":True, "load": True, "field": "RESGUARDO"},
                {"name": "INSTITUCION_BIENESTAR_ORIGEN", "type": "string" , "size":"12", "clean":True, "load": True, "field": "INSTITUCION_BIENESTAR_ORIGEN"},
                {"name": "COD_JOR", "type": "string" , "size":"2", "clean":True, "load": True, "field": "COD_JOR"},
                {"name": "JORNADA", "type": "string" , "size":"10", "clean":True, "load": True, "field": "JORNADA"},
                {"name": "COD_CARACTER", "type": "string" , "size":"2", "clean":True, "load": True, "field": "COD_CARACTER"},
                {"name": "CARACTER", "type": "string" , "size":"10", "clean":True, "load": True, "field": "CARACTER"},
                {"name": "COD_ESP", "type": "string" , "size":"3", "clean":True, "load": True, "field": "COD_ESP"},
                {"name": "ESPECIALIDADES", "type": "string" , "size":"10", "clean":True, "load": True, "field": "ESPECIALIDADES"},
                {"name": "COD_GRADO", "type": "string" , "size":"2", "clean":True, "load": True, "field": "COD_GRADO"},
                {"name": "GRADO", "type": "string" , "size":"10", "clean":True, "load": True, "field": "GRADO"},
                {"name": "COD_GRUPO", "type": "string" , "size":"4", "clean":True, "load": True, "field": "COD_GRUPO"},
                {"name": "COD_MET", "type": "string" , "size":"2", "clean":True, "load": True, "field": "COD_MET"},
                {"name": "METODOLOGIAS", "type": "string" , "size":"14", "clean":True, "load": True, "field": "METODOLOGIAS"},
                {"name": "MATRICULA_CONTRATADA", "type": "string" , "size":"2", "clean":True, "load": True, "field": "MATRICULA_CONTRATADA"},
                {"name": "REPITENTE", "type": "string" , "size":"2", "clean":True, "load": True, "field": "REPITENTE"},
                {"name": "NUEVO", "type": "string" , "size":"2", "clean":True, "load": True, "field": "NUEVO"},
                {"name": "COD_FTE_REC", "type": "string" , "size":"2", "clean":True, "load": True, "field": "COD_FTE_REC"},
                {"name": "FUENTE_RECURSO", "type": "string" , "size":"3", "clean":True, "load": True, "field": "FUENTE_RECURSO"},
                {"name": "COD_ZONA_ALU", "type": "string" , "size":"2", "clean":True, "load": True, "field": "COD_ZONA_ALU"},
                {"name": "ZONA_RESIDE_ALUMNO", "type": "string" , "size":"8", "clean":True, "load": True, "field": "ZONA_RESIDE_ALUMNO"},
                {"name": "CAB_FAMILIA", "type": "string" , "size":"2", "clean":True,"load": True, "field": "CAB_FAMILIA"},
                {"name": "BEN_MAD_FLIA", "type": "string" , "size":"2", "clean":True, "load": True, "field": "BEN_MAD_FLIA"},
                {"name": "BEN_VET_FP", "type": "string"  , "size":"2", "clean":True, "load": True, "field": "BEN_VET_FP"},
                {"name": "BEN_HER_NAC", "type": "string" , "size":"2", "clean":True, "load": True, "field": "BEN_HER_NAC"},
                {"name": "CODIGO_INTERNADO", "type": "string" , "size":"2", "clean":True, "load": True, "field": "CODIGO_INTERNADO"},
                {"name": "INTERNADO", "type": "string" , "size":"2", "clean":True, "load": True, "field": "INTERNADO"},
                {"name": "CODIGO_VALORACION_1", "type": "string" , "size":"2", "clean":True, "load": True, "field": "CODIGO_VALORACION_1"},
                {"name": "CODIGO_VALORACION_2", "type": "string" , "size":"2", "clean":True, "load": True, "field": "CODIGO_VALORACION_2"},
                {"name": "NUM_CONVENIO", "type": "string" , "size":"2", "clean":True, "load": True, "field": "NUM_CONVENIO"},
                {"name": "PER_ID", "type": "string" , "size":"10", "clean":True, "load": True, "field": "PER_ID"},
                {"name": "FEC_CORTE", "type": "date" , "size":"9", "clean":True, "load": True ,"field": "FEC_CORTE","format": "%d-%m-%Y"},
                {"name": "NIVEL", "type": "string" , "size":"14", "clean":True, "load": True, "field": "NIVEL"},
                {"name": "CALENDARIO", "type": "string" , "size":"1", "clean":True, "load": True, "field": "CALENDARIO"},
                {"name": "PRESTADOR 2022", "type": "string" , "size":"10", "clean":True, "load": True, "field": "PRESTADOR 2022"},
                {"name": "NUMERO CONTRATO", "type": "string" , "size":"10", "clean":True, "load": True, "field": "NUMERO CONTRATO"},
                {"name": "POBLACION", "type": "string" , "size":"14", "clean":True, "load": True, "field": "POBLACION"},
                {"name": "Region", "type": "string" , "size":"6", "clean":True, "load": True, "field": "Región"},
                {"name": "caracter", "type": "string" , "size":"12", "clean":True, "load": True, "field": "carácter"},
                {"name": "APOYO_ACADEMICO_ESPECIAL", "type": "string" , "size":"2", "clean":True},
                {"name": "SRPA", "type": "string" , "size":"2", "clean":True, "load": True, "field": "SRPA"},
                {"name": "PAIS_ORIGEN", "type": "string" , "size":"3", "clean":True, "load": True, "field": "PAIS_ORIGEN"},
                {"name": "NACIONALIDAD", "type": "string" , "size":"10", "clean":True, "load": True, "field": "NACIONALIDAD"},
                {"name": "TRASTORNOS_ESPECIFICOS", "type": "string","size":"2", "clean":True , "load": True, "field": "TRASTORNOS_ESPECIFICOS"},
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

