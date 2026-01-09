"""
==================================================
        EXCEPCIONES EN MANEJO DE ARCHIVOS
==================================================

Este archivo muestra cómo manejar errores
relacionados con archivos utilizando:

- Rutas absolutas
- Rutas relativas
- Bloque with open (forma recomendada)
"""

import os

# ==================================================
#             LECTURA CON RUTA ABSOLUTA
# ==================================================


def leer_archivo_ruta_absoluta():
    """
    Especifica la ubicación completa del archivo
    desde la raíz del sistema.
    """
    ruta_absoluta = ("D:/Cursos/Python/Intermediate/07-Exceptions-ErrorHandling/EEH02_example.txt")

    try:
        archivo = open(ruta_absoluta, "r", encoding="utf-8")
        contenido = archivo.read()
        print(contenido)

    except FileNotFoundError:
        print("Error: no se encontró el archivo.")

    finally:
        archivo.close()
        print("El archivo se cerró correctamente.\n")

# ==================================================
#             LECTURA CON RUTA RELATIVA
# ==================================================

def leer_archivo_ruta_relativa():
    """
    Especifica la ubicación del archivo
    relativa al directorio actual.
    """
    archivo_ruta = "Intermediate/07-Exceptions-ErrorHandling/EEH02_example.txt"

    try:
        archivo = open(archivo_ruta, "r", encoding="utf-8")
        contenido = archivo.read()
        ruta_absoluta = os.path.abspath(archivo_ruta)

        print(contenido)
        print(f"Ruta absoluta del archivo: {ruta_absoluta}")

    except FileNotFoundError:
        print("Error: no se encontró el archivo.")

    finally:
        archivo.close()
        print("El archivo se cerró correctamente.\n")

# ==================================================
#       LECTURA CON WITH OPEN (RECOMENDADO)
# ==================================================


def leer_archivo_with_open():
    """
    Manejo de archivos usando 'with open'.
    El archivo se cierra automáticamente,
    incluso si ocurre una excepción.
    """
    archivo_ruta = "Intermediate/07-Exceptions-ErrorHandling/EEH02_example.txt"

    try:
        with open(archivo_ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            print(contenido)

    except FileNotFoundError:
        print("Error: no se encontró el archivo.")

# leer_archivo_ruta_absoluta()
# leer_archivo_ruta_relativa()
leer_archivo_with_open()