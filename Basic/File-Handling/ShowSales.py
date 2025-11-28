"""
Mostrar Reporte de Ventas

- Lee el archivo "ventas.txt".
- Muestra cada venta registrada.
- Si el archivo no existe, muestra un mensaje de advertencia.
"""

def mostrar_reporte_ventas():
    print("Reporte de ventas del día:")

    try:
        # Abre el archivo en modo lectura
        with open("Basic/File-Handling/ventas.txt", "r") as archivo:
            contenido = archivo.readlines()  # Lee todas las líneas

            if contenido:
                for linea in contenido:
                    print(linea.strip())  # Elimina saltos de línea extra
            else:
                print("El archivo está vacío. No se encontraron ventas registradas.")

    except FileNotFoundError:
        print("No se encontró el archivo 'ventas.txt'. Asegúrese de que forme parte del proyecto.")


# Ejemplo de uso
mostrar_reporte_ventas()