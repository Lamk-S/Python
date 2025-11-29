"""
Bucle FOR
---------
Utilice el bucle `for` cuando conozca la cantidad de veces que se repetirá
un proceso. Este tipo de bucle es útil para iterar sobre rangos de números,
listas, cadenas u otros elementos iterables en Python.
"""

# Ejemplo 1: Iterar sobre un rango de números
# for num in range(5, 10):
#     print(f"{num} - Bienvenido al curso de Python")
# print("Fin del bucle")

# Ejemplo 2: Iterar sobre elementos de una lista
# frutas = ["manzana", "banana", "cereza"]
# for fruta in frutas:
#     print(fruta)

# Ejemplo 3: Iterar sobre caracteres de una cadena
# mensaje = "Bienvenido al curso de Python"
# for letra in mensaje:
#     print(letra)

# Ejemplo 4: Sumar números ingresados por el usuario
suma_numeros = 0
cont_num = 0

for x in range(1, 6):  # Se repetirá 5 veces (del 1 al 5)
    numeros_ing = int(input("Ingrese un número: "))
    suma_numeros = suma_numeros + numeros_ing
    cont_num = cont_num + 1

print(f"La suma total es {suma_numeros} y el número de vueltas es {cont_num}")