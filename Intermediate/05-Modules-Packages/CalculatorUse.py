"""
Módulo: CalculatorUse
Descripción:
    Ejemplo de cómo utilizar un paquete personalizado llamado Calculator.
    El paquete contiene módulos separados para realizar operaciones básicas:
    suma, resta, multiplicación y división.

Estructura del paquete:
    Calculator/
        __init__.py
        Addition.py
        Subtraction.py
        Multiplication.py
        Division.py

Este archivo importa las funciones desde cada módulo y ejecuta un ejemplo
práctico de uso dentro de la función main().
"""

# -----------------------------------------------------------
# Importación de funciones desde el paquete Calculator
# -----------------------------------------------------------
from Calculator.Addition import sumar
from Calculator.Subtraction import restar
from Calculator.Multiplication import multiplicar
from Calculator.Division import dividir

# -----------------------------------------------------------
# Función para solicitar y validar entrada numérica del usuario
# -----------------------------------------------------------
def pedir_numero(mensaje: str) -> float:
    """Pide un número al usuario y lo valida. Repite hasta obtener uno válido."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número.")

# -----------------------------------------------------------
# Función principal del programa
# -----------------------------------------------------------
def main():
    a = pedir_numero("Ingrese el primer número 'a': ")
    b = pedir_numero("Ingrese el segundo número 'b': ")

    try:
        print(f"Suma: {a} + {b} = {sumar(a, b)}")
        print(f"Resta: {a} - {b} = {restar(a, b)}")
        print(f"Multiplicación: {a} * {b} = {multiplicar(a, b)}")
        print(f"División: {a} / {b} = {dividir(a, b)}")
    except (TypeError, ValueError) as error:
        print(f"Error: {error}")

# -----------------------------------------------------------
# Punto de entrada del programa
# -----------------------------------------------------------
if __name__ == "__main__":
    main()