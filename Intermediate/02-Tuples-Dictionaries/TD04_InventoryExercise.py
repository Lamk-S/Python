"""
Ejercicio: Sistema básico de inventario
---------------------------------------

Este programa maneja un inventario utilizando diccionarios anidados.
Incluye funciones para listar, agregar, eliminar, actualizar precios
y consultar productos dentro del inventario.
"""

# ---------------------------------------------------------------
# Inventario inicial
# ---------------------------------------------------------------

inventario = {
    "Manzanas": {"cantidad": 50, "precio": 0.5},
    "Naranjas": {"cantidad": 30, "precio": 0.7},
    "Plátanos": {"cantidad": 20, "precio": 0.3},
    "Peras": {"cantidad": 15, "precio": 0.6},
    "Toronjas": {"cantidad": 40, "precio": 1.0}
}


# ---------------------------------------------------------------
# Funciones de gestión del inventario
# ---------------------------------------------------------------

def listar_inventario(inventario):
    print("Inventario Actual:")
    for producto, detalles in inventario.items():
        print(f"{producto}: Cantidad = {detalles['cantidad']}, Precio = S/.{detalles['precio']}")
        
def agregar_producto(inventario, nombre, cantidad, precio):
    if nombre in inventario:
        inventario[nombre]['cantidad'] += cantidad
    else:
        inventario[nombre] = {"cantidad": cantidad, "precio": precio}
    print(f"Producto '{nombre}' agregado/actualizado.")

def eliminar_producto(inventario, nombre):
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado.")
    else:
        print(f"Producto '{nombre}' no encontrado en el inventario.")

def actualizar_precio(inventario, nombre, nuevo_precio):
    if nombre in inventario:
        inventario[nombre]['precio'] = nuevo_precio
        print(f"Precio del producto '{nombre}' actualizado a S/.{nuevo_precio}.")
    else:
        print(f"Producto '{nombre}' no encontrado en el inventario.")
        
def consultar_producto(inventario, nombre):
    if nombre in inventario:
        producto = inventario[nombre]
        print(f"{nombre}: Cantidad = {producto['cantidad']}, Precio = S/.{producto['precio']}")
    else:
        print(f"Producto '{nombre}' no encontrado en el inventario.")


# ---------------------------------------------------------------
# Ejecución de pruebas
# ---------------------------------------------------------------

agregar_producto(inventario, "Kiwis", 25, 1.2)
eliminar_producto(inventario, "Plátanos")
actualizar_precio(inventario, "Naranjas", 0.75)

producto = input("\nIngrese el nombre del producto a consultar: ")
consultar_producto(inventario, producto)

listar_inventario(inventario)