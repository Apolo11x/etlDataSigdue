import os

folders = [
    "data/raw",
    "data/processed",
    "etl",
    "logs",
    "tests"
]

files = {
    "etl/extract.py": "# Extracción de datos\n",
    "etl/transform.py": "# Transformación y limpieza de datos\n",
    "etl/load.py": "# Carga de datos a Oracle\n",
    "etl/utils.py": "# Funciones auxiliares\n",
    "etl/config.py": "# Configuración del proyecto\n",
    "tests/test_extract.py": "# Pruebas para extract.py\n",
    "tests/test_transform.py": "# Pruebas para transform.py\n",
    "tests/test_load.py": "# Pruebas para load.py\n",
    "requirements.txt": "# Lista de dependencias\n",
    "main.py": "# Script principal para ejecutar el ETL\n",
    "README.md": "# ETL Data SIGDUE\n"
}

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file_path, content in files.items():
    with open(file_path, "w") as f:
        f.write(content)

print("Estructura de proyecto creada exitosamente.")