"""
Programación modular
"""

# -----------------------------------------------------------
# 1. Importar funciones específicas
# -----------------------------------------------------------
# from Utilities import mensaje_bienvenida, calcular_edad, contar_vocales
#
# print(mensaje_bienvenida("admin", "1234", "Lamk"))
# calcular_edad()
# contar_vocales()

# -----------------------------------------------------------
# 2. Importar todo el módulo
# -----------------------------------------------------------
# import Utilities
#
# print(Utilities.mensaje_bienvenida("admin", "1234", "Lamk"))
# Utilities.calcular_edad()
# Utilities.contar_vocales()
#
# objeto = Utilities.MiClase("Lamk")
# objeto.saludar()

# -----------------------------------------------------------
# 3. Importar con alias (recomendado en proyectos reales)
# -----------------------------------------------------------
# import Utilities as util

# print(util.mensaje_bienvenida("admin", "1234", "Lamk"))
# util.calcular_edad()
# util.contar_vocales()

# objeto = util.MiClase("Lamk")
# objeto.saludar()

# -----------------------------------------------------------
# Notas rápidas:
# -----------------------------------------------------------
"""
- from modulo import X
    ✓ Acceso directo a funciones
    ✗ Puede sobrescribir nombres

- import modulo
    ✓ Más claro al leer el código
    ✓ Evita conflictos de nombres

- import modulo as alias
    ✓ Estilo limpio y profesional
    ✓ Muy usado cuando el módulo es largo (ej: numpy as np)
"""