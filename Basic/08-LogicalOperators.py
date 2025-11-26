"""
===========================================
   Operadores Relacionales y Lógicos
===========================================

Los operadores relacionales devuelven valores booleanos (True / False)
al comparar dos expresiones.

Operadores Relacionales:
    ==   Igualdad
    !=   Desigualdad
    >    Mayor que
    <    Menor que
    >=   Mayor o igual que
    <=   Menor o igual que

Operadores Lógicos:
    and  → Devuelve True solo si ambas expresiones son verdaderas.
    or   → Devuelve True si al menos una expresión es verdadera.
    not  → Niega una expresión booleana.
"""

# ===========================================
# Ejemplos con operadores relacionales
# ===========================================

nombre_persona = "Melvin"
nombre_empleado = "Melvin"
esta_logeado = False

# Comparación de igualdad
respuesta = nombre_persona == nombre_empleado
print(respuesta)  # True

# Comparación de desigualdad
respuesta_2 = True != esta_logeado
print(respuesta_2)  # True


# ===========================================
# Ejemplo práctico con operadores lógicos
# ===========================================

edad_persona = 24
tiene_licencia = True

puedo_conducir = edad_persona >= 18 and tiene_licencia
print(puedo_conducir)  # True


# ===========================================
# Más ejemplos de operadores relacionales
# ===========================================

a = 10
b = 20
c = 10

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= c)   # True
print(a <= c)   # True


# ===========================================
# Ejemplo usando condicionales
# ===========================================

if a < b and a == c:
    print("a es menor que b y a es igual a c")
else:
    print("La condición no se cumple")