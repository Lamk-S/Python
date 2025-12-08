"""
---------------------------------------------------------
Tuplas en Python
---------------------------------------------------------

Las tuplas son estructuras inmutables, es decir, sus valores
no pueden modificarse una vez creadas. No permiten agregar,
eliminar ni alterar elementos directamente.

Sintaxis para crear una tupla:
    my_tuple = (valor1, valor2, ...)
    my_tuple = tuple()      # tupla vacía
    my_tuple = ()           # otra forma de definir una tupla vacía
---------------------------------------------------------
"""

# ---------------------------------------------------------
# Formas de definir una tupla
# ---------------------------------------------------------
my_tuple = tuple()
my_tuple2 = ()

print(type(my_tuple))
print(type(my_tuple2))

# Ejemplo de tupla con distintos tipos de datos
my_tuple = (10, "hola", 3.14, [1, 2, 3, 4])

# ---------------------------------------------------------
# Inmutabilidad de las tuplas
# ---------------------------------------------------------
# Las tuplas no permiten:
# my_tuple.append(10)   # Incorrecto
# my_tuple[2] = 20      # Incorrecto

# ---------------------------------------------------------
# Modificar una tupla convirtiéndola temporalmente en lista
# ---------------------------------------------------------
my_tuple3 = (1, 2, 3, 4)
list_tuple = list(my_tuple3)   # Conversión a lista
list_tuple.append(5)           # Modificación permitida
my_tuple4 = tuple(list_tuple)  # Conversión de vuelta a tupla

print(my_tuple4)
print(my_tuple3)  # La original permanece igual (inmutable)

# ---------------------------------------------------------
# Métodos y slicing en tuplas
# ---------------------------------------------------------
my_tuple5 = (1, 2, 2, 2, 3, 4)

# count(): cuenta las apariciones de un valor
print(my_tuple5.count(2))
print(my_tuple5.count(3))

# Slicing en tuplas
subTuple = my_tuple5[1:4]   # Desde índice 1 hasta 3
subTuple2 = my_tuple5[:3]   # Primeros 3 elementos
subTuple3 = my_tuple5[2:]   # Desde índice 2 hasta el final
subTuple4 = my_tuple5[::2]  # Saltos de 2 en 2
subTuple5 = my_tuple5[::-1] # Tupla invertida

print(subTuple)
print(subTuple2)
print(subTuple3)
print(subTuple4)
print(subTuple5)