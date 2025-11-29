"""
Bucle WHILE
-----------
Utilice el bucle `while` cuando se deba repetir un bloque de código mientras
se cumpla una condición lógica.

Sintaxis:
while condicion:
    # Bloque de código
"""

# Ejemplo 1: Contador simple
"""
contador = 0
while contador < 5:
    print(contador)
    contador += 1
"""

# Ejemplo 2: Suma progresiva hasta alcanzar un límite
"""
suma = 0
n = 1

while suma < 20:
    suma += n
    n += 1

print(f"La suma es {suma}")
"""

# Ejemplo 3: Sistema básico de autenticación con intentos
usuario_valido = "lamk"
pass_valida = "admin"
intentos = 3
persona = "Melvin López"

while intentos > 0:
    usuario = input("Ingrese el usuario: ")
    password = input("Ingrese la contraseña: ")

    if usuario == usuario_valido and password == pass_valida:
        print(f"Inicio de sesión exitoso. Bienvenido al sistema, {persona}. ¡Un gusto tenerlo aquí!")
        break
    else:
        intentos -= 1
        print(f"Usuario o contraseña incorrectos. Intentos restantes: {intentos}")

if intentos == 0:
    print("Tu cuenta se bloqueará por 24 horas.")