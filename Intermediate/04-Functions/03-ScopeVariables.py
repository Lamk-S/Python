# ----------------------------------------
# Ejemplo 1: Uso de una variable global
# ----------------------------------------

# Variable global
x = 10

def mi_funcion():
    # Variable local
    y = 5
    print(f"Valor de x dentro de la función: {x}")  # Acceso a variable global
    print(f"Valor de y dentro de la función: {y}")  # Acceso a variable local

mi_funcion()


# ----------------------------------------
# Ejemplo 2: Modificar una variable global
# ----------------------------------------

contador = 0  # Variable global

def incrementar_contador():
    global contador
    contador += 1
    print(f"Dentro de incrementar_contador, contador = {contador}")

incrementar_contador()


# ----------------------------------------
# Ejemplo 3: Aplicación sencilla para seguimiento de usuarios
# ----------------------------------------

# Variable global para llevar el registro de usuarios activos
usuarios_activos = 0

def iniciar_sesion(nombre_usuario):
    global usuarios_activos
    usuarios_activos += 1
    print(f"Usuario {nombre_usuario} inició sesión.")
    print(f"Número de usuarios activos: {usuarios_activos}")

def cerrar_sesion(nombre_usuario):
    global usuarios_activos
    usuarios_activos -= 1
    print(f"Usuario {nombre_usuario} cerró sesión.")
    print(f"Número de usuarios activos: {usuarios_activos}")


# Simulación de inicio y cierre de sesión de usuarios
iniciar_sesion("Lamk")
iniciar_sesion("Alice")
cerrar_sesion("Lamk")
iniciar_sesion("Bob")
cerrar_sesion("Alice")
cerrar_sesion("Bob")