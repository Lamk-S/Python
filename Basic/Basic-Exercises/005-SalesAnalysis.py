"""
Descripción
-----------
Realizar un análisis de ventas a partir de un archivo CSV que contiene un
registro con las columnas:

- Fecha
- Producto
- Cantidad
- Precio

El objetivo es generar:
1. Un resumen del total de ventas por producto.
2. El ingreso total por día.
"""

import csv
from collections import defaultdict


def analizar_ventas(archivo_csv: str) -> None:
    ventas_por_producto = defaultdict(float)
    ingresos_por_dia = defaultdict(float)

    try:
        with open(archivo_csv, mode="r", encoding="utf-8") as file:
            lector_csv = csv.DictReader(file)

            for fila in lector_csv:
                try:
                    producto = fila["Producto"]
                    fecha = fila["Fecha"]
                    cantidad = int(fila["Cantidad"])
                    precio = float(fila["Precio"])

                    total_venta = cantidad * precio

                    ventas_por_producto[producto] += total_venta
                    ingresos_por_dia[fecha] += total_venta
                except (ValueError, KeyError) as e:
                    print(f"Error en el formato de una fila: {fila} -> {e}")
                    continue

    except FileNotFoundError:
        print(f"Error: el archivo '{archivo_csv}' no se encuentra.")
        return
    except PermissionError:
        print(f"Error: no tienes permisos para abrir el archivo '{archivo_csv}'.")
        return
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
        return

    # -------------------------------------------------------------
    # Mostrar los resultados
    # -------------------------------------------------------------
    print("===============================================")
    print(" Total de ventas por producto ")
    print("===============================================")
    for producto, total in ventas_por_producto.items():
        print(f"{producto}: ${total:.2f}")

    print("\n===============================================")
    print(" Ingresos totales por día ")
    print("===============================================")
    for fecha, total in ingresos_por_dia.items():
        print(f"{fecha}: ${total:.2f}")


# -----------------------------
# Ejemplo de uso
# -----------------------------

archivo_csv = "Basic\\Basic-Exercises\\ventas.csv"
analizar_ventas(archivo_csv)