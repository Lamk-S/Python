"""
Comprensión de diccionarios
------------------------------------------------------

Sintaxis general:

    {clave: valor for item in iterable if condicion}

Permite crear diccionarios de manera compacta y eficiente.
"""

# ---------------------------------------------------------------
# Crear un diccionario con números y sus cuadrados
# ---------------------------------------------------------------
cuadrados = {x: x**2 for x in range(6)}
print(f"Cuadrados: {cuadrados}")

# ---------------------------------------------------------------
# Crear un diccionario solo con números pares
# ---------------------------------------------------------------
pares = {x: x for x in range(11) if x % 2 == 0}
print(f"Pares: {pares}")

# ---------------------------------------------------------------
# Crear un diccionario con números pares y sus cuadrados
# ---------------------------------------------------------------
cuadrados_pares = {x: x**2 for x in range(11) if x % 2 == 0}
print(f"Cuadrados pares: {cuadrados_pares}")

# ---------------------------------------------------------------
# Invertir claves y valores en un diccionario existente
# ---------------------------------------------------------------
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
invertido = {v: k for k, v in mi_diccionario.items()}
print(f"Diccionario invertido: {invertido}")

# ---------------------------------------------------------------
# Crear un diccionario a partir de una lista de tuplas
# ---------------------------------------------------------------
tuplas = [('a', 10), ('b', 20), ('c', 30)]
diccionario_desde_tuplas = {k: v for k, v in tuplas}
print(f"Diccionario desde tuplas: {diccionario_desde_tuplas}")

# ---------------------------------------------------------------
# Crear un diccionario usando únicamente claves
# ---------------------------------------------------------------
claves = ['x', 'y', 'z']
diccionario_desde_claves = {k: 0 for k in claves}
print(f"Diccionario desde claves: {diccionario_desde_claves}")

# ---------------------------------------------------------------
# Crear un diccionario combinando claves y valores usando zip()
# ---------------------------------------------------------------
valores = [100, 200, 300]
diccionario_desde_claves_valores = {k: v for k, v in zip(claves, valores)}
print(f"Diccionario desde claves y valores: {diccionario_desde_claves_valores}")