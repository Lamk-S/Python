import csv

# ============================
#   Lectura de archivos CSV
# ============================
def extraer_datos_csv():
    contador = 0
    with open('Intermediate\\05-Modules-Packages\\MP03_products.csv', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        # Iterar sobre las filas del archivo CSV
        for fila in lector_csv:
            if contador>0:
                print(fila)
            contador += 1
        print(f"Total filas leídas: {contador}")

# ============================
#   Lectura de archivos TXT
# ============================
def extraer_datos_txt():
    with open('Intermediate\\05-Modules-Packages\\MP03_information.txt', encoding='utf-8') as archivo_txt:
        contenido = archivo_txt.read()
        print(contenido)

# ============================
#   Escritura de archivos CSV
# ============================
def generar_archivo():
    try:
        data_to_write = [
            ['CODIGO', 'PRODUCTO', 'STOCK'],
            ['001', 'Manzanas', '50'],
            ['002', 'Naranjas', '75'],
            ['003', 'Platanos', '100'],
            ['004', 'Peras', '60'],
            ['005', 'Uvas', '80']            
        ]
        with open('Intermediate\\05-Modules-Packages\\MP03_new_products.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data_to_write)
    except Exception as e:
        print(f"Ocurrió un error al generar el archivo: {e}")
    else:
        print("Archivo generado correctamente.")
    finally:
        file.close()