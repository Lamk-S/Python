"""
En este ejercicio se simula un sistema de inventario con dos 
almacenes y se realizan operaciones para:

    - Encontrar productos comunes
    - Encontrar productos exclusivos de cada almacén
    - Obtener la lista total de productos disponibles
"""

# -------------------------------------------------------------------
# Definición de los almacenes
# -------------------------------------------------------------------
almacen1 = {"laptop", "monitor", "teclado", "raton", "impresora"}
almacen2 = {"tablet", "monitor", "teclado", "altavoces", "webcam"}

# -------------------------------------------------------------------
# Productos comunes entre ambos almacenes
# -------------------------------------------------------------------
comunes = almacen1.intersection(almacen2)
print("Productos comunes en ambos almacenes:", comunes)

# -------------------------------------------------------------------
# Productos exclusivos de cada almacén
# -------------------------------------------------------------------
exclusivos_almacen1 = almacen1.difference(almacen2)
exclusivos_almacen2 = almacen2.difference(almacen1)

print("Productos exclusivos del Almacén 1:", exclusivos_almacen1)
print("Productos exclusivos del Almacén 2:", exclusivos_almacen2)

# -------------------------------------------------------------------
# Lista completa de todos los productos
# -------------------------------------------------------------------
todos_productos = almacen1.union(almacen2)
print("Todos los productos disponibles en ambos almacenes:", todos_productos)