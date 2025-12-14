# ------------------------------
# Definición de conjuntos
# ------------------------------
conjunto = {1, 2, 3, 4, 5}
conjunto2 = set([1, 2, 3, 4, 5])  # Alternativa usando set()

print(type(conjunto))    # <class 'set'>
print(type(conjunto2))   # <class 'set'>

# ------------------------------
# Métodos básicos de los sets
# ------------------------------
conjunto.add(6)           # Agregar un elemento
conjunto.remove(3)        # Eliminar un elemento (error si no existe)
conjunto.discard(10)      # Eliminar sin error aunque no exista

print("Conjunto actualizado:", conjunto)

# pop() elimina y devuelve un elemento arbitrario del set
elemento_eliminado = conjunto.pop()
print(f"Elemento eliminado con pop(): {elemento_eliminado}")
print("Conjunto luego de pop():", conjunto)

# ------------------------------
# Operaciones entre conjuntos
# ------------------------------
frutas = {"manzana", "banana", "cereza", "naranja"}
citrus = {"naranja", "limón", "lima"}

print("\nFrutas:", frutas)

print("Unión (union):", frutas.union(citrus))
print("Intersección (intersection):", frutas.intersection(citrus))
print("Diferencia frutas - citrus:", frutas.difference(citrus))
print("Diferencia citrus - frutas:", citrus.difference(frutas))
print("Diferencia simétrica:", frutas.symmetric_difference(citrus))

# Los sets eliminan automáticamente duplicados
frutas = {"manzana", "banana", "cereza", "naranja", "banana"}
print("\nFrutas sin duplicados:", frutas)

# ------------------------------
# Operaciones con operadores
# ------------------------------
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

diferencia = conjunto_a - conjunto_b
print("\nDiferencia (a - b):", diferencia)

diferencia2 = conjunto_b - conjunto_a
print("Diferencia (b - a):", diferencia2)

interseccion = conjunto_a & conjunto_b
print("Intersección (a & b):", interseccion)

union = conjunto_a | conjunto_b
print("Unión (a | b):", union)

diferencia_simetrica = conjunto_a ^ conjunto_b
print("Diferencia simétrica (a ^ b):", diferencia_simetrica)