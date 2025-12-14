"""
Ejercicio: Actualizar y eliminar elementos en un diccionario
-----------------------------------------------------------

En este ejemplo se crea un diccionario, se actualizan claves existentes,
se agregan nuevas claves y se eliminan elementos usando diferentes métodos.
"""

# Diccionario inicial
d = {'a': 1, 'b': 5}

# update(): permite actualizar claves existentes o agregar nuevas
d.update({'a': 24, 'b': 2, 'c': 3})

# popitem(): elimina y retorna el último par clave-valor insertado
item = d.popitem()

print("Elemento eliminado con popitem():", item)
print("Diccionario luego de popitem():", d)

# ---------------------------------------------------------------
# Crear diccionarios
# ---------------------------------------------------------------

my_dictionary = {}          # Diccionario vacío
my_dictionary2 = dict()     # Otra forma de crear un diccionario vacío

# Diccionario con información de ejemplo
my_dictionary = {
    "nombre": "Melvin",
    "edad": 24,
    "ciudad": "Trujillo"
}

# ---------------------------------------------------------------
# Acceso a valores y métodos útiles
# ---------------------------------------------------------------

print(my_dictionary.get("nombre"))  # Acceder al valor de la clave 'nombre'
print(my_dictionary.items())        # Obtener pares clave-valor
print(my_dictionary.keys())         # Obtener todas las claves
print(my_dictionary.values())       # Obtener todos los valores

# ---------------------------------------------------------------
# Agregar y actualizar elementos
# ---------------------------------------------------------------

my_dictionary["profesion"] = "Developer Full Stack"  # Agregar nueva clave
my_dictionary["nombre"] = "Melvin Kevin"             # Actualizar clave existente

print("Diccionario actualizado:", my_dictionary)

# ---------------------------------------------------------------
# Eliminar elementos
# ---------------------------------------------------------------

del my_dictionary["profesion"]   # Eliminar la clave 'profesion'
print("Luego de eliminar 'profesion':", my_dictionary)

# ---------------------------------------------------------------
# Recorrer un diccionario
# ---------------------------------------------------------------

for k, v in my_dictionary.items():
    print(f"La clave '{k}' tiene el valor '{v}'")