"""
Aplicar un descuento a un producto dependiendo de su precio:
 - Precio > 100  ---> descuento del 10%
 - Precio <= 100 ---> descuento del 5%
"""

precio = float(input("Introducir el precio del producto: "))

# Condicional para determinar el descuento
if precio > 100:
    descuento = precio * 0.10
else:
    descuento = precio * 0.05

# El precio final es precio menos el descuento
precio_final = precio - descuento

print(f"Descuento aplicado: ${descuento:.2f}")
print(f"El precio final con descuento es: ${precio_final:.2f}")