"""
==================================================
                ABSTRACCIÓN EN POO
==================================================

La abstracción permite definir una estructura
común (interfaz) que las clases hijas deben
implementar, sin especificar los detalles
concretos de cómo lo hacen.
"""

from abc import ABC, abstractmethod
import math

# ==================================================
#               CLASE ABSTRACTA BASE
# ==================================================

class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        "Método abstracto para calcular el área de la forma"
        pass
    def __str__(self):
        """Método para presentar la forma como una cadena"""
        return f"{self.__class__.__name__} con área: {self.calcular_area()}"

# ==================================================
#               CLASES CONCRETAS
# ==================================================
    
class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        """Calcular el área del círculo"""
        return math.pi * (self.radio ** 2)

class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    def calcular_area(self):
        """Calcula el área del rectángulo"""
        return self.ancho * self.alto

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        """Calcular el área del triángulo"""
        return (self.base * self.altura) / 2
    
# ==================================================
#           FUNCIÓN QUE USA ABSTRACCIÓN
# ==================================================

def mostrar_area(forma):
    print(forma)

# ==================================================
#                 EJEMPLOS DE USO
# ==================================================

# Crear instancias de las subclases
mi_circulo = Circulo(radio = 5)
mi_rectangulo = Rectangulo(ancho = 5, alto = 3)
mi_triangulo = Triangulo(base = 10, altura = 5)

# Todas las formas responden al mismo método
mostrar_area(mi_circulo)
mostrar_area(mi_rectangulo)
mostrar_area(mi_triangulo)