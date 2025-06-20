# Configuración del proyecto
import os

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