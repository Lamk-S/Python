"""
==================================================
        EJERCICIO PRÁCTICO: GESTIÓN DE EMPLEADOS
==================================================

Este ejercicio refuerza los conceptos de:
- Herencia
- Polimorfismo
- Uso de métodos sobrescritos
- Buenas prácticas en POO
"""

# ==================================================
#               CLASE BASE
# ==================================================

class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario
    def mostrar_info(self):
        return f"Nombre: {self.nombre}\nPuesto: {self.puesto}\nSalario: {self.salario:.2f}"
    def tipo_empleado(self):
        return "Empleado Regular"

# ==================================================
#               SUBCLASE GERENTE
# ==================================================

class Gerente(Empleado):
    def __init__(self, nombre, salario, bonus):
        super().__init__(nombre, "Gerente", salario)
        self.bonus = bonus
    def mostrar_info(self):
        info = super().mostrar_info()
        return f"{info}\nBonus: {self.bonus}"
    def tipo_empleado(self):
        return "Gerente"

# ==================================================
#        FUNCIÓN POLIMÓRFICA
# ==================================================

def mostrar_informacion_empleados(empleados):
    for empleado in empleados:
        print(empleado.mostrar_info())
        print(f"Tipo de Empleado: {empleado.tipo_empleado()}")
        print("-" * 35)

# ==================================================
#                 EJEMPLOS DE USO
# ==================================================


# Crear empleados regulares
empleado1 = Empleado("Ana Torres", "Desarrolladora", 3500)
empleado2 = Empleado("Luis Pérez", "Soporte Técnico", 2800)

# Crear gerente
gerente = Gerente("Carlos Gómez", salario=6000, bonus=1500)

# Crear una lista de empleados que incluye tanto empleados regulares como gerentes
lista_empleados = [empleado1, empleado2, gerente]

# Mostrar la información de todos los empleados en la lista
mostrar_informacion_empleados(lista_empleados)