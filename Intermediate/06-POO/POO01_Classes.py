"""
-------------------------------------------------------------------
Introducción a la Programación Orientada a Objetos (POO) en Python.
-------------------------------------------------------------------
"""

# ===========================================
#           Definición de una clase
# ===========================================

"""
Una clase funciona como una plantilla o molde para crear objetos.

A partir de esta clase se pueden crear múltiples instancias (objetos),
cada una con sus propios valores para los atributos definidos.
"""

class Persona:
    """
    Constructor de la clase.
    __init__:
        Es un método especial que se ejecuta automáticamente cuando
        se crea una nueva instancia de la clase.
    Parámetros:
        nombre (str): Nombre de la persona.
        edad (int): Edad de la persona.
    self:
        Es una parámetro que hace referencia a la instancia actual de la
        clase y permite acceder a los atributos y métodos del objeto.
    """
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # ===========================================
    #             Métodos de la clase
    # ===========================================
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
    
# ===========================================
#     Creación de objetos (instanciación)
# ===========================================
persona1 = Persona("Lamk", 24)
persona2 = Persona("Angie", 21)

# ===========================================
#             Uso de los objetos
# ===========================================
print("Datos de persona1:")
print(persona1.nombre, persona1.edad)
print(persona1.saludar())
print("Atributos internos:", persona1.__dict__)

print("\nDatos de persona2:")
print(persona2.nombre, persona2.edad)
print(persona2.saludar())
print("Atributos internos:", persona2.__dict__)