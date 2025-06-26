# Configuración del proyecto
import os
import json

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


def get_initial_config(file_type):
        """
        Retorna una configuración inicial en formato JSON para el tipo de archivo especificado.
        """
        configs = {
            "csv": {
                "delimiter": ",",
                "encoding": "utf-8",
                "has_header": True,
                "fields": [
                    {"name": "campo1", "type": "string"},
                    {"name": "campo2", "type": "int"},
                    {"name": "campo3", "type": "float"}
                ]
            },
            "json": {
                "encoding": "utf-8",
                "fields": [
                    {"name": "campo1", "type": "string"},
                    {"name": "campo2", "type": "int"},
                    {"name": "campo3", "type": "float"}
                ]
            }
        }
        config = configs.get(file_type.lower())
        if config is None:
            raise ValueError(f"Tipo de archivo no soportado: {file_type}")
        return json.dumps(config, indent=4, ensure_ascii=False)