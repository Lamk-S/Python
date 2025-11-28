"""
===========================================
                Condicionales
===========================================
"""

"""
Sintaxis básica:

if condition:
    pass
else:
    pass

Con múltiples condiciones:

if condition:
    pass
elif condition:
    pass
else:
    pass
"""

# Ejemplo 1: Condicional simple
"""
x = float(input("Ingrese el valor de x: "))

if x > 0:
    print("X es positivo")
elif x == 0:
    print("X es cero")
else:
    print("X es negativo")
"""

# Ejemplo 2: Condicionales anidados (nested)
"""
x = 15
y = 10

if x > 0:
    if y > 0:
        print("Ambos x e y son positivos")
    else:
        print("x es positivo, pero y no es positivo")
else:
    print("x no es positivo")
"""

# Ejemplo 3: Uso de operadores lógicos (and)
"""
x = 20
y = 30

if x > 10 and y < 40:
    print("x es mayor que 10 e y es menor que 40")
"""

# Ejemplo 4: Uso de operadores lógicos (or, not)
"""
x = 5
y = 15

if x < 10 or y > 10:
    print("Al menos una de las condiciones es verdadera")

if not (x > 10):
    print("x no es mayor que 10")
"""

# Ejemplo 5: Manejo de errores con try/except
"""
try:
    punt_obt = float(input("Ingrese el puntaje obtenido: "))

    if punt_obt > 150:
        print("Eres un Master en Python")
    elif 100 < punt_obt <= 150:
        print("Tienes un nivel Senior")
    elif 70 < punt_obt <= 100:
        print("Tienes un nivel Intermedio")
    else:
        print("Tienes un nivel Básico")

except ValueError:
    print("Debes ingresar un valor numérico")
"""

# Ejemplo final: Cálculo de promedio con sustitutorio
nota_uno = float(input("Ingrese la nota uno: "))
nota_dos = float(input("Ingrese la nota dos: "))
nota_tres = float(input("Ingrese la nota tres: "))

prom_notas = (nota_uno + nota_dos + nota_tres) / 3

if prom_notas >= 10.5:
    print("Felicitaciones, APROBASTE el curso")
else:
    nota_sus = float(input("Ingrese la nota sustitutoria: "))
    nuevo_prom = (nota_sus + prom_notas) / 2

    if nuevo_prom >= 10.5:
        print(f"El alumno aprobó el curso usando el sustitutorio: {round(nuevo_prom, 2)}")
    else:
        print(f"El alumno deberá llevar nuevamente el curso: {round(nuevo_prom, 2)}")