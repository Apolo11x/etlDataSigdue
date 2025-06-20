# ETL Data SIGDUE

Este proyecto tiene como objetivo desarrollar un proceso de Extracción, Transformación y Carga (ETL) de datos para la aplicación SIGDUE. Actualmente, SIGDUE utiliza una base de datos Oracle 11G R2 para almacenar su información principal.

## Objetivos principales:

1. **Extracción:** Tomar datos desde archivos ubicados en una carpeta específica del sistema.
2. **Análisis y Preparación:** Analizar los archivos, preparar y limpiar los datos, asegurando su calidad y consistencia.
3. **Comparativa:** Comparar la estructura y contenido de los datos extraídos con las estructuras existentes en la base de datos Oracle de SIGDUE.
4. **Carga:** Cargar los datos procesados en la base de datos, cumpliendo con los requerimientos funcionales y estructurales necesarios para el correcto funcionamiento de la aplicación SIGDUE.

## Alcance:

- Automatización del flujo de datos desde archivos fuente hasta la base de datos destino.
- Validación y limpieza de datos para evitar inconsistencias.
- Adaptación de los datos a los formatos y estructuras requeridas por SIGDUE.
- Registro de logs y manejo de errores durante el proceso ETL.

## Estructura del Proyecto

etlDataSigdue/
│
├── data/                # Carpeta datos fuente y procesados
│   ├── raw/             # Datos originales sin procesar
│   ├── processed/       # Datos ya transformados/listos para cargar
│
├── etl/                 # Código fuente del proceso ETL
│   ├── extract.py       # Funciones extracción de datos
│   ├── transform.py     # Funciones transform y limpieza
│   ├── load.py          # Funciones para carga a Oracle
│   ├── utils.py         # Utilidades y funciones auxiliares
│   └── config.py        # Config general del proyecto
│
├── logs/                # Archivos logs del proceso ETL
│
├── tests/               # Pruebas unit y de integración
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
│
├── requirements.txt     # Dependencias del proyecto
├── README.md            # Documentación principal
└── main.py              # Script principal ETL

- **data/raw/**: Archivos de datos originales.
- **data/processed/**: Archivos de datos transformados y listos para cargar.
- **etl/**: Código fuente del proceso ETL (extracción, transformación, carga y utilidades).
- **logs/**: Archivos de registro del proceso ETL.
- **tests/**: Pruebas unitarias y de integración.
- **requirements.txt**: Dependencias del proyecto.
- **main.py**: Script principal para ejecutar el proceso ETL.

## Requisitos

- Python 3.8+
- Oracle Client (instantclient)
- Paquetes listados en `requirements.txt`

## Ejecución

1. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

2. Ejecuta el proceso ETL:
    ```bash
    python main.py
    ```

## Descripción General

El proceso ETL realiza las siguientes tareas:
- Extrae datos desde archivos ubicados en `data/raw/`.
- Limpia y transforma los datos según las reglas de negocio.
- Compara y valida la estructura de los datos con la base de datos Oracle.
- Carga los datos procesados en la base de datos SIGDUE.

## Contacto

Para dudas o sugerencias, contacta al equipo de SISE