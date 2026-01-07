"""
==================================================
            ENCAPSULACIÓN EN POO
==================================================

La encapsulación consiste en restringir el
acceso directo a los atributos internos de
una clase y obligar a interactuar con ellos
mediante métodos públicos.

En Python, esto se logra usando atributos
"privados" con doble guion bajo (__).
"""

# ==================================================
#               CLASE CUENTA BANCARIA
# ==================================================

class CuentaBancaria:
    """
    Representa una cuenta bancaria con saldo
    protegido mediante encapsulación.
    """
    
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        # Atributo definido como privado
        self.__saldo = saldo_inicial
        
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Deposito exitoso. Nuevo saldo: ${self.__saldo:.2f}")
        else:
            print("EL mnto a depositar debe ser positivo")
            
    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: ${self.__saldo:.2f}")
        else:
            print("Monto invalido o saldo insuficiente")
            
    def consultar_saldo(self):
        return f"Saldo actual: #{self.__saldo:.2f}"
    
# ==================================================
#                 EJEMPLO DE USO
# ==================================================
    
# Crear una cuenta Bancaria
cuenta = CuentaBancaria("Melvin López", 2000)

# Intentar modificar el saldo directamente (no recomendado)
try:
    cuenta.__saldo = 5000 # No lanza error, crea un nuevo atributo
except AttributeError as e:
    print(f"Error: {e}")

# El saldo real permanece protegido
print(cuenta.consultar_saldo())

# Interacción correcta usando métodos públicos
cuenta.depositar(500)
print(cuenta.consultar_saldo())

cuenta.retirar(250)
print(cuenta.consultar_saldo())