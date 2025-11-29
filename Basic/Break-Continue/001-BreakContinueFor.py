"""
Uso de Break y Continue en un Bucle FOR
"""

# Ejemplo 1: Buscar un número en una lista y detener el bucle con break
"""
numeros = [1, 3, 5, 7, 9, 11, 13, 15]
objetivo = int(input("Ingrese el objetivo: "))

for numero in numeros:
    if numero == objetivo:
        print(f"Número {objetivo} encontrado.")
        break
else:
    print("Número no encontrado.")
"""

# Ejemplo 2: Imprimir los números de una lista omitiendo los pares
"""
Imprime solo los números impares de la lista usando continue.
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for numero in numeros:
    if numero % 2 == 0:
        continue  # Saltar los números pares
    print(numero)