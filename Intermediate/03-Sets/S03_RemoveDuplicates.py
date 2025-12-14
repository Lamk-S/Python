# -------------------------------------------------------------
# 1. Eliminar duplicados de una lista
# -------------------------------------------------------------

lista = [1, 2, 2, 3, 4, 4, 5, 1, 6]

# Convertir a set para eliminar duplicados
conjunto = set(lista)

# Convertir de vuelta a lista
lista_sin_duplicados = list(conjunto)

print("Lista original:", lista)
print("Lista sin duplicados:", lista_sin_duplicados)


# -------------------------------------------------------------
# 2. Encontrar elementos comunes entre dos conjuntos
# -------------------------------------------------------------

def elementos_comunes(conjunto1, conjunto2):
    return conjunto1 & conjunto2

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}

comunes = elementos_comunes(conjunto_a, conjunto_b)
print("\nConjunto A:", conjunto_a)
print("Conjunto B:", conjunto_b)
print("Elementos comunes:", comunes)