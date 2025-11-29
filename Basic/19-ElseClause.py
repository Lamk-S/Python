"""
Cláusula ELSE en Bucles
-----------------------
En Python, la cláusula `else` puede utilizarse junto con los bucles `for` y `while`.
El bloque dentro de `else` se ejecuta únicamente cuando el bucle finaliza de forma
"natural", es decir, sin haber utilizado la instrucción `break`.

Uso típico:
for elemento in iterable:
    # Bloque del bucle
else:
    # Se ejecuta cuando el bucle termina sin interrupción

while condicion:
    # Bloque del bucle
else:
    # Se ejecuta cuando la condición se vuelve falsa
"""

# Ejemplo 1: Uso de else con un bucle FOR
"""
frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print(fruta)
else:
    print("Se han procesado todas las frutas.")
"""

# Ejemplo 2: Uso de else con un bucle WHILE
contador = 0

while contador < 3:
    print(contador)
    contador += 1
else:
    print("El bucle ha terminado porque la condición es falsa.")