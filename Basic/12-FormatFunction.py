"""
===========================================
              Función format()
===========================================

La función format() permite insertar valores dentro de una cadena
de texto. También permite dar formato a números, como limitar
decimales, alinear texto, agregar relleno, etc.

Sintaxis:
    "texto {}".format(valor)
    "texto {0} y {1}".format(v1, v2)
    "texto {variable}".format(variable=valor)

Equivalente moderno:
    f"texto {variable}"
"""

nombre_usuario = "Melvin"
saludo = "Hola, {}".format(nombre_usuario)
print(saludo)

# ===========================================
# Formato de números
# ===========================================

pi = 3.14159

formated_pi = "El valor de pi es {:.2f}".format(pi)  # 2 decimales
print(formated_pi)

# ===========================================
# Equivalente usando f-strings
# ===========================================

nombre_persona = "Angie"
saludo = f"Hola, {nombre_persona}"
print(saludo)