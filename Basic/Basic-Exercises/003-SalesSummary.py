"""
Descripción
-----------
Dado un registro de ventas diarias representado como una lista de
diccionarios, generar un resumen con:

1. El total de ventas en dinero.
2. La cantidad total de artículos vendidos.
"""


def resumen_ventas(ventas: list) -> tuple:
    # Paso 1: Inicializar contadores
    total_ventas = 0
    total_articulos = 0

    # Paso 2: Recorrer la lista de ventas
    for venta in ventas:
        total_ventas += venta["precio"] * venta["cantidad"]
        total_articulos += venta["cantidad"]

    # Paso 3: Devolver resultados
    return total_ventas, total_articulos


# -----------------------------
# Ejemplo de uso
# -----------------------------

ventas = [
    {"precio": 10, "cantidad": 2},
    {"precio": 5, "cantidad": 4},
    {"precio": 20, "cantidad": 1},
]

total_ventas, total_articulos = resumen_ventas(ventas)

print(f"Total de ventas: ${total_ventas}")
print(f"Total de artículos vendidos: {total_articulos}")