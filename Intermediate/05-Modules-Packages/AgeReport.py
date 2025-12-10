"""
Crear un archivo en formato CSV con datos provenientes de una lista.
Sumar los datos numéricos (edades) y colocar los resultados (total y promedio)
en filas adicionales al final del archivo.
"""

# -----------------------------------------------------------
# Importación de módulos
# -----------------------------------------------------------
import csv
import gc

# Ejecuta la recolección de basura para liberar memoria
gc.collect()

# -----------------------------------------------------------
# Definición del nombre del archivo de salida
# -----------------------------------------------------------
nombre_archivo = 'Intermediate/05-Modules-Packages/age_report.csv'


# -----------------------------------------------------------
# Datos de ejemplo
# Cada elemento es una fila: [NOMBRE, EDAD]
# -----------------------------------------------------------
datos = [
    ['NOMBRE', 'EDAD'],
    ['Juan', 28],
    ['María', 34],
    ['Pedro', 22],
    ['Ana', 45],
    ['Luis', 30]
]

# -----------------------------------------------------------
# Cálculo de estadísticas (Total y Promedio)
# -----------------------------------------------------------

# Se suman solo las edades, excluyendo la fila de encabezado
total_edades = sum(row[1] for row in datos[1:])

# Cálculo del promedio de edades
promedio_edades = total_edades / (len(datos) - 1)

# Se agregan las filas finales con el total y el promedio
datos.append(['TOTAL', total_edades])
datos.append(['PROMEDIO', round(promedio_edades, 2)])  # Se redondea a 2 decimales

# -----------------------------------------------------------
# Escritura del archivo CSV
# -----------------------------------------------------------
with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(datos)

# -----------------------------------------------------------
# Lectura y visualización del archivo generado
# -----------------------------------------------------------
with open(nombre_archivo, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
