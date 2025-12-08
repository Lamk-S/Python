# -----------------------------------------------------------
# Mensaje de bienvenida
# -----------------------------------------------------------
def mensaje_bienvenida(user, password, nombre=None):
    if user == "admin" and password == "1234":
        return f"Bienvenido, {nombre}!"
    else:
        return f"Usuario {nombre} Invalido"

# -----------------------------------------------------------
# Cálculo de edad
# -----------------------------------------------------------
from datetime import date

def calcular_edad():
    fecha_nacimiento = date.fromisoformat(input("Ingrese su fecha de nacimiento (YYYY-MM-DD): "))
    hoy = date.today()
    edad = hoy.year - fecha_nacimiento.year
    if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    return print(f"Tu edad es: {edad}")

# -----------------------------------------------------------
# Contar vocales en un texto
# -----------------------------------------------------------
def contar_vocales():
    texto = input("Ingrese una frase: ").lower()
    vocales = "aeiou"
    contador = 0
    for letra in texto:
        if letra in vocales:
            contador += 1
    return print(f"El número de vocales es: {contador}")

# -----------------------------------------------------------
# Clase de ejemplo
# -----------------------------------------------------------
class MiClase:
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self):
        return print(f"Hola, mi nombre es {self.nombre}!")