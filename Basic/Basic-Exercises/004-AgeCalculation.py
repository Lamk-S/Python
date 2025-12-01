"""
Descripción
-----------
Dada una fecha de nacimiento, calcular la edad actual de la persona.
"""

from datetime import date


def calcular_edad(fecha_nacimiento: date) -> int:
    # Paso 1: Obtener la fecha actual
    hoy = date.today()

    # Paso 2: Calcular diferencia inicial de años
    edad = hoy.year - fecha_nacimiento.year

    # Paso 3: Ajustar si el cumpleaños aún no ha ocurrido este año
    if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1

    return edad


# -----------------------------
# Ejemplo de uso
# -----------------------------

fecha_nacimiento = date(2001, 9, 13)
print(f"Edad actual: {calcular_edad(fecha_nacimiento)} años")