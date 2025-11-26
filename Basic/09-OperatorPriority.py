"""
===========================================
          Prioridad de Operadores
===========================================

En Python, los operadores tienen un orden de evaluación (precedencia).
Esto determina qué operaciones se realizan primero.

Orden de prioridad (de mayor a menor):

1. Paréntesis:                ( )
2. Exponentes:                **
3. Signos unarios:            +a   -a   not
4. Multiplicación, división:  *   /   //   %
5. Suma y resta:              +   -
6. Comparaciones:             >   <   >=   <=   ==   !=
7. Operadores lógicos:        not → and → or
"""

# ===========================================
# Ejemplos prácticos de precedencia
# ===========================================

# 1. Paréntesis
resultado = (3 + 2) * 4
# Primero se evalúa (3+2) = 5, luego 5 * 4 = 20
print(resultado)  # 20

# 2. Exponente
resultado2 = 2 ** 3
# 2 elevado a 3 = 8
print(resultado2)  # 8

# 3. Signo unario
resultado3 = -5 + 3
# Primero se interpreta -5, luego -5 + 3 = -2
print(resultado3)  # -2

# 4. Multiplicación y división (de izquierda a derecha)
resultado4 = 10 / 2 * 3
# 10 / 2 = 5.0, luego 5.0 * 3 = 15.0
print(resultado4)  # 15.0

# 5. Suma y resta
resultado5 = 10 + 5 - 3
# Primero 10 + 5 = 15, luego 15 - 3 = 12
print(resultado5)  # 12

# 6. Comparaciones
resultado6 = 5 + 3 > 6
# Primero 5 + 3 = 8, luego 8 > 6 = True
print(resultado6)  # True

# 7. Operadores lógicos
resultado7 = True and not False
# Primero se evalúa: not False = True
# Luego: True and True = True
print(resultado7)  # True