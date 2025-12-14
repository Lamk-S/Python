"""
def nombre_funcion(parametros):
    # Cuerpo de la función
    pass
"""

# ---------------------------------------------------------
# 1. Definición básica de funciones
# ---------------------------------------------------------

def mi_primera_funcion():
    pass  # Esta función no hace nada

def sumar(a, b):
    return a + b

suma = sumar(3, 5)
print(f"La suma es: {suma}")

# ---------------------------------------------------------
# 2. Funciones con parámetros de texto
# ---------------------------------------------------------

def mensaje_bienvenida(nombre):
    salida = f"¡Hola, {nombre}! Bienvenido/a al curso de Python."
    print(salida)


mensaje_bienvenida("Lamk")


def saludar_invitado(nombre="Invitado"): # Parámetro con valor por defecto
    salida = f"¡Hola, {nombre}!"
    return salida


print(saludar_invitado("Lamk"))


# ---------------------------------------------------------
# 3. Funciones anidadas
# ---------------------------------------------------------

def externa():
    def interna():
        return "¡Hola desde la función interna!"

    return interna()


print(externa())


# ---------------------------------------------------------
# 4. Funciones lambda
# ---------------------------------------------------------

multiplicar = lambda x, y: x * y  # Función anónima
print(f"El resultado de la multiplicación es: {multiplicar(4, 6)}")


# ---------------------------------------------------------
# 5. Documentación con docstrings
# ---------------------------------------------------------

def restar_ahora(a, b):
    """
    Resta dos números y devuelve el resultado.
    """
    return a - b


# ---------------------------------------------------------
# 6. Ejemplo adicional de funciones anidadas
# ---------------------------------------------------------

def calculadora_minima(x, y):
    def suma(a, b):
        return a + b

    def resta(a, b):
        return a - b

    return suma(x, y), resta(x, y)


resultado_suma, resultado_resta = calculadora_minima(10, 5)
print(f"Suma: {resultado_suma}, Resta: {resultado_resta}")