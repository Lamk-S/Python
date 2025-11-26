"""
===========================================
               Función input()
===========================================
"""

# ===========================================
# Ejemplo práctico usando input()
# ===========================================

nombre_producto = input("Ingrese el nombre del producto: ")

precio_producto = float(input("Ingrese el precio del producto: "))

cantidad_producto = int(input("Ingrese la cantidad del producto: "))

# Cálculo del total
total = precio_producto * cantidad_producto

# Resultados
print(f"El total a pagar es: {total}")
print(f"Tipo de dato del nombre: {type(nombre_producto)}")
print(f"Tipo de dato del precio: {type(precio_producto)}")
print(f"Tipo de dato de la cantidad: {type(cantidad_producto)}")
print(f"Tipo de dato del total: {type(total)}")