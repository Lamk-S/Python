# ---------------------------------------------------------
# 1. Argumentos Posicionales
# ---------------------------------------------------------

def suma_valores(a, b, c):
    return a + b + c
resultado = suma_valores(5, 10, 15)
print("Suma de valores:", resultado)

# ---------------------------------------------------------
# 2. Argumentos Nombrados (Keyword Arguments)
# ---------------------------------------------------------

def describir_persona(nombre, edad):
    return f"{nombre} tiene {edad} años."
descripcion = describir_persona(edad = 24, nombre = "Lamk")
print(descripcion)

# ---------------------------------------------------------
# 3. Argumentos por Defecto
# ---------------------------------------------------------

def mensaje_bienvenida(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}!"
mensaje1 = mensaje_bienvenida("Lamk")
mensaje2 = mensaje_bienvenida("Lamk", saludo="Bienvenido")
print(mensaje1)
print(mensaje2)

# ---------------------------------------------------------
# 4. Argumentos Variables
# ---------------------------------------------------------
# *args = Captura argumentos posicionales adicionales como tupla
# **kwargs = Captura argumentos nombrados adicionales como diccionario

def sumar_valores_dos(*args):
    return sum(args)

resultado_dos = sumar_valores_dos(1, 2, 3, 4, 5)
print("Suma de valores variables:", resultado_dos)

def mostrar_informacion(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_informacion(nombre="Lamk", edad=24, ciudad="Trujillo")


# ---------------------------------------------------------
# 5. Argumentos Combinados
# ---------------------------------------------------------
# Orden correcto:
# 1. Argumentos posicionales
# 2. Argumentos con valor por defecto
# 3. *args
# 4. **kwargs

def funcion_combinada(a, b=10, *args, **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
    
funcion_combinada(5, 20, 1, 2, 3, nombre="Lamk", edad=24)