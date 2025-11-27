"""
===========================================
 Manejo de Archivos (File Handling)
===========================================
"""

# 'r'  : Leer (read). El archivo **debe existir**.
# 'w'  : Escribir (write). Crea el archivo o lo sobrescribe.
# 'a'  : Anexar (append). Crea el archivo si no existe y escribe al final.
# 'b'  : Modo binario (binary). Se combina: 'rb', 'wb', 'ab'.
# 'x'  : Creación exclusiva. Falla si el archivo ya existe.

# =====================================================
# 1. Ejemplo: Leer un archivo existente ('r')
# =====================================================

# Descomenta estas líneas si tienes el archivo "informacion.txt"
# with open('informacion.txt', 'r', encoding='utf-8') as file:
#     contenido = file.read()
#     print("Contenido del archivo:")
#     print(contenido)


# =====================================================
# 2. Ejemplo: Escribir un archivo nuevo ('w')
# =====================================================

# Si el archivo existe → se sobrescribe
# Si no existe → se crea automáticamente
with open('informacion.txt', 'w', encoding='utf-8') as file:
    file.write("Primera línea de texto\n")
    file.write("Segunda línea de texto\n")

print("Archivo 'informacion.txt' creado y escrito exitosamente.")