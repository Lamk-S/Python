"""
--------------------------------------------------------------
Herencia en Programación Orientada a Objetos (POO) con Python
--------------------------------------------------------------

¿QUÉ ES LA HERENCIA?
    - Es un principio de la POO que permite crear nuevas clases
    a partir de clases existentes.
    
    - La clase hija hereda losatribos y métodos de la clase
    padre, permitiendo reutilizar código y extender su 
    funcionalidad.
 
La función "super()" se utiliza para llamar métodos de la clase
padre desde una clase hija.
"""

class Vehiculo:
    def __init__(self, marca: str, modelo: str, año: int):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def mostrar_informacion(self) -> str:
        return f"{self.marca} {self.modelo} ({self.año})"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, numero_puertas):
        # Llamada al constructor de la clase base
        super().__init__(marca, modelo, año)
        self.numero_puertas = numero_puertas
    
    def mostrar_informacion(self):
        base_info = super().mostrar_informacion()
        return f"{base_info}, # Puertas: {self.numero_puertas}"

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, tipo_motor):
        # Llamada al constructor de la clase base
        super().__init__(marca, modelo, año)
        self.tipo_motor = tipo_motor
    
    def mostrar_informacion(self):
        base_info = super().mostrar_informacion()
        return f"{base_info}, Motor: {self.tipo_motor}"
        
# ============================
# Ejemplo de uso
# ============================

# Crear instancias de las clases derivadas
coche = Coche("Toyota", "Corolla", 2020, 4)
motocicleta = Motocicleta("Harley-Davidson", "Iron 883", 2023, "V-TWIN")

# Mostrar la información de los vehículos
print(coche.mostrar_informacion())
print(motocicleta.mostrar_informacion())