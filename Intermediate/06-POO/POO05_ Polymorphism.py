"""
==================================================
                POLIMORFISMO EN POO
==================================================

El polimorfismo permite que diferentes clases
implementen un mismo método de formas distintas,
siempre que compartan una interfaz común.
"""

# ==================================================
#                     CLASE BASE
# ==================================================

class Animal:
    """
    Clase base que define la interfaz común
    para todos los animales.
    """
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser sobreescrito por las subclases")
    
    def __str__(self):
        return f"Nombre({self.nombre}) , Edad({self.edad})"

# ==================================================
#                 CLASES DERIVADAS
# ==================================================
    
class Perro(Animal):
    def hacer_sonido(self):
        return "Ladrido"
    
class Gato(Animal):
    def hacer_sonido(self):
        return "Maullido"
    
class Vaca(Animal):
    def hacer_sonido(self):
        return "Mugido"


# ==================================================
#         FUNCIÓN POLIMÓRFICA
# ==================================================

# Acepta cualquier objeto que sea una instancia
# de Animal (o de sus subclases) y ejecuta
# el mismo método sin conocer su tipo concreto.

def hacer_sonido_animal(animal):
    print(f"{animal} hace: {animal.hacer_sonido()}")
    
# ==================================================
#                 USO DEL POLIMORFISMO
# ==================================================

# Crear instancias de diferentes subclases
mi_perro = Perro(nombre="Wolf", edad=5)
mi_gato = Gato(nombre="Cheto", edad=1)
mi_vaca = Vaca(nombre="Manchas", edad=3)


# Todas las instancias responden al mismo método,
# pero con comportamientos distintos
hacer_sonido_animal(mi_perro)
hacer_sonido_animal(mi_gato)
hacer_sonido_animal(mi_vaca)