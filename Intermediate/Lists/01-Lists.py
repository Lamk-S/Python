# -------------------------------
# Creación y manipulación de listas en Python
# -------------------------------

# Modos para crear una lista vacía
valores = []           # Forma literal
valores = list()       # Forma usando el constructor de la clase list

# Creación de una lista con distintos tipos de datos
valores = [1200, 1900, 1700, "Juan", True, [1200, 90]]

# Se ha creado una lista denominada 'frutas'
frutas = ["manzana", "banana", "cereza"]

# Acceso a elementos de la lista mediante índices
print(valores[0])   # Devuelve el valor de la posición 0
print(valores[-1])  # Devuelve el último valor de la lista

# Agregar elementos a la lista
valores.append("Lamk")  # Agrega el valor "Lamk" al final de la lista

# Inserción de elementos en una posición específica
# Inserta el valor "Maria" en la posición 2; los demás valores se desplazan a la derecha
valores.insert(2, "Maria")
print(valores)

# Eliminación de elementos
valores.pop(2)         # Elimina el elemento de la posición 2
valores.remove("Lamk") # Elimina la primera aparición del valor "Lamk"
print(valores)

# Modificación de elementos
valores[2] = 1900  # Se edita el valor ubicado en la posición 2
print(valores)

# Cantidad de elementos en la lista
cant_ele = len(valores)        # Indica la cantidad total de elementos
cant_1900 = valores.count(1900) # Indica cuántas veces aparece el valor 1900

print(f"La cantidad de elementos de la lista es {cant_ele}")
print(f"El valor 1900 se repite {cant_1900} veces")

# ---------------------------------------------------------
# Operaciones comunes con listas
# ---------------------------------------------------------

frutas = ["manzana", "banana", "cereza"]  # Lista de frutas

# Ordenar la lista
frutas.sort()  # Ordena los elementos alfabéticamente
print(frutas)

# Ordenar en orden inverso
frutas.reverse()  # Invierte el orden de los elementos
print(frutas)

# Recorrer una lista con un bucle for
for fruta in frutas:
    print(fruta)