"""
Crear un programa que determine si un número es par o impar.
"""

numero = int(input("Introducir un número: "))

# Condicional simple
if numero % 2 == 0:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")