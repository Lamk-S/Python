"""
===========================================
 Métodos de Cadena (String Methods)
===========================================
"""

# =====================================================
# 1. Convertir texto a mayúsculas y minúsculas
# =====================================================

nombre_curso = "Python"

nueva_cadena = nombre_curso.upper()   # Convierte todo a MAYÚSCULAS
nueva_cadena_dos = nombre_curso.lower()  # Convierte todo a minúsculas

print("Upper:", nueva_cadena)
print("Lower:", nueva_cadena_dos)


# =====================================================
# 2. Eliminar espacios al inicio y al final (strip)
# =====================================================

mensaje = " Hola mundo "
nueva_cadena_tres = mensaje.strip()  # Quita espacios iniciales y finales

print("Strip:", nueva_cadena_tres)


# =====================================================
# 3. Buscar texto dentro de una cadena (find, index)
# =====================================================

mensaje_bien = "hola mundo desde Python"

# find() devuelve el índice o -1 si NO encuentra el texto
indice_find = mensaje_bien.find("Python")

# index() devuelve el índice pero lanza ValueError si NO encuentra el texto
indice_index = mensaje_bien.index("Python")

print("Find:", indice_find)
print("Index:", indice_index)


# =====================================================
# 4. Reemplazar texto dentro de una cadena (replace)
# =====================================================

mensaje_bien = "Hola mundo desde Python"
cadena_reemplazar = mensaje_bien.replace("Python", "Django")

print("Replace:", cadena_reemplazar)


# =====================================================
# 5. Unir elementos de una lista para formar una cadena (join)
# =====================================================

palabras = ["manzana", "banana", "cereza"]

resultado = ", ".join(palabras)  # Une elementos con coma y espacio
print("Join:", resultado)