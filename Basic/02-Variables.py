""" 
Ejemplos de declaración de variables
"""

# Asignación simple

nom_per = "Melvin"
ape_per = "López"
edad_per = 24
sue_per = 1499.90
act_per = True

# Asignaciones múltiples

cant_prod, msj_bien, estado = 5, "hola", True
# print(msj_bien,cant_prod)

# Asignar el mismo valor a varias variables

x = y = z = 10
# print(x)
# print(y)
# print(z)

# Tipos de Datos especiales (Estructura de Datos)
"""
LIST
DICCIONARIOS
TUPLAS
CONJUNTOS
"""

# List -> lista
cursos = ["Python","DJango","Flask",20,45.32,["Docker","Pandas"]]

# Dict -> Diccionario
empleados = {
    "CODIGO": "200", "NOMBRE": "LAMK", "APELLIDO": "SINES",
}
# print(empleados["CODIGO"])

# Tuple -> Tupla
# Son inmutables - no se pueden modificar ni agregar un nuevo valor
valores = (100, 200, 300)
# valores.append(20)

# Set -> Conjuntos
datos = {12,45,67,89}
# print(datos)

# Muestra cuales son las palabras reservadas del lenguaje
import keyword
# print(keyword.kwlist)