"""
---------------------------------------------------------
List Comprehension | Compresión de Listas en Python
---------------------------------------------------------

Ventajas:
- Más compacto y fácil de leer cuando la operación es simple.
- Ideal para transformaciones rápidas sobre un iterable.
- Sintaxis general:
      [expresion for elemento in iterable if condicion]

Método Tradicional:
- Más claro cuando se necesita lógica compleja o varios pasos.
- Recomendado para procesos más elaborados.
---------------------------------------------------------
"""

# ---------------------------------------------------------
# Ejemplo 1: Elevar números al cuadrado
# ---------------------------------------------------------

# Usando List Comprehension
cuadrados = [x**2 for x in range(10)]
print(cuadrados)
print(type(cuadrados))

# Usando método tradicional
cuadrados_trad = []
for x in range(10):
    cuadrados_trad.append(x**2)
print(cuadrados_trad)


# ---------------------------------------------------------
# Ejemplo 2: Filtrar números pares
# ---------------------------------------------------------

numeros = list(range(1, 11))

# Usando List Comprehension
pares = [x for x in numeros if x % 2 == 0]
print(pares)

# Usando método tradicional
pares_trad = []
for x in numeros:
    if x % 2 == 0:
        pares_trad.append(x)
print(pares_trad)


# ---------------------------------------------------------
# Ejemplo 3: Obtener longitudes de palabras
# ---------------------------------------------------------

palabras = ["Python", "Django", "Flask"]

# Usando List Comprehension
longitudes = [len(palabra) for palabra in palabras]
print(longitudes)

# Usando método tradicional
longitudes_trad = []
for palabra in palabras:
    longitudes_trad.append(len(palabra))
print(longitudes_trad)
