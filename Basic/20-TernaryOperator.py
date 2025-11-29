"""
Operadores Ternarios (Condicionales en una sola línea)
------------------------------------------------------
El operador ternario permite evaluar una condición en una sola línea y devolver
uno de dos valores posibles.

Sintaxis:
valor_si_verdadero if condicion else valor_si_falso
"""

# Ejemplo 1: Verificar mayoría de edad
"""
edad = 17
mensaje = "Eres adulto" if edad >= 18 else "Eres menor de edad"
print(mensaje)
"""

# Ejemplo 2: Determinar si un número es par o impar
"""
numero = 7
resultado = "Par" if numero % 2 == 0 else "Impar"
print(resultado)
"""

# Ejemplo 3: Ternario anidado (múltiples condiciones)
nota = 60

resultado = (
    "Excelente" if nota >= 90
    else "Buena" if nota >= 70
    else "Necesita mejorar"
)

print(resultado)