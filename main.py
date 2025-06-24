
from etl.etl_anexo_6a import procesar_anexo_6a

# Ejemplo de uso de la función etl_anexo_6a
# Supongamos que la función recibe una ruta de archivo de entrada y una de salida


input_file = 'ANEXO_6A_CORTE_01062025.csv'
output_file = 'processed_ANEXO_6A_CORTE_01062025.csv'

procesar_anexo_6a(input_file, output_file, ';')