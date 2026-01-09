"""
==================================================
        EXCEPCIONES PERSONALIZADAS Y ASSERT
==================================================
"""

# ==================================================
#                       RAISE
# ==================================================
"""
- Se utiliza para lanzar una excepciónde forma
explícita.
- Se emplea cuando el programa detecta una condición
inválida y necesita interrumpir el flujo normal de
ejecución.
"""

# ==================================================
#           EXCEPCIÓN PERSONALIZADA
# ==================================================

class MiError(Exception):
    """
    Excepción personalizada para errores de validación.
    """
    def __init(self, mensaje):
        super.__init__(mensaje)
        
def verificar_edad(edad):
    """
    Verifica que la edad sea válida.
    Lanza una excepción personalizada si la condición
    no se cumple.
    """
    if edad < 0:
        raise MiError("La edad no puede ser negativa.")
    return edad

# ==================================================
#       RAISE CON EXCEPCIONES NATIVAS
# ==================================================   
    
def dividir(a, b):
    """
    Divide dos números.
    Lanza ZeroDivisionError si el divisor es cero.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    return a / b

# ==================================================
#                       ASSERT
# ==================================================
"""
Se usa para comprobar condiciones que deberían ser
verdaderas en tiempo de desarrollo y puede ayudar a
detectar errores en etapas tempranas.
"""

def calcular_media(lista):
    assert len(lista) > 0, "La lista no puede estar vacía."
    return sum(lista) / len(lista)

# ==================================================
#               EJEMPLOS DE USO
# ==================================================

# print("=== Excepción personalizada ===")
# try:
#     print(verificar_edad(25))
#     print(verificar_edad(-3))
# except MiError as err:
#     print(f"Error personalizado: {err}")

# print("\n=== Raise con excepción nativa ===")
# try:
#     resultado = dividir(10, 0)
# except ZeroDivisionError as err:
#     print(f"Error de división: {err}")

# print("\n=== Uso de assert ===")
# try:
#     edad = int(input("Ingrese la edad: "))
#     assert edad > 0, "La edad debe ser un número positivo."
#     print("Edad ingresada correctamente.")
# except (ValueError, AssertionError) as err:
#     print(f"Error: {err}")

# print("\n=== Uso de assert con calcular_media ===")
# try:
#     numeros = [10, 20, 30, 40]
#     print(f"Media de {numeros}: {calcular_media(numeros)}")
#     lista_vacia = []
#     print(f"Media de lista vacía: {calcular_media(lista_vacia)}")
# except AssertionError as err:
#     print(f"Error de validación: {err}")