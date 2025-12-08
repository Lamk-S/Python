"""
Estructura general de una función recursiva:

def funcion_recursiva(parametors):
    # Caso base
    if condicion_base:
        return resultado_base
    else:
        # Llamada recursiva
        return funcion_recursiva(parametros_modificados)
"""

# -----------------------------------------------------------
# Definición: Cálculo del factorial utilizando recursividad
# -----------------------------------------------------------
# El factorial de un número entero n (n!) se define como:
#   Caso base: 0! = 1
#   Caso recursivo: n! = n * (n - 1)!
#
# Ejemplo:
#   5! = 5 * 4 * 3 * 2 * 1 = 120
# -----------------------------------------------------------
def factorial(n):
    # Caso base
    if n == 0:
        return 1
    else:
        # Llamada recursiva
        return n * factorial(n - 1)

# Ejemplo de uso
print(factorial(5))  # Salida: 120