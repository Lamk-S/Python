"""
==================================================
        MANEJO DE EXCEPCIONES EN PYTHON
==================================================

Estructura básica:

- try:
    Contiene el código que puede generar una excepción.
- except:
    Captura y maneja la excepción si ocurre.
- else (opcional):
    Se ejecuta si NO ocurre ninguna excepción.
- finally (opcional):
    Se ejecuta siempre, ocurra o no una excepción.
"""

# ==================================================
#     EJEMPLO 01: TRY / EXCEPT / ELSE / FINALLY
# ==================================================

def ejemplo_exception_001():
    try:
        numero_ingresado = int(input("Ingrese un valor entero: "))
        resultado = numero_ingresado / 0  # Error forzado
    except Exception as err:
        print("Ocurrió la siguiente excepción:", err)
    else:
        print("No ocurrió ninguna excepción.")
    finally:
        print("Se terminó la ejecución.\n")

# ==================================================
#               TIPOS DE ERRORES
# ==================================================
    
"""
1. Errores de sintaxis (SyntaxError)
   Se detectan antes de ejecutar el programa.

   Ejemplo (NO ejecutar):
       estado = False,
       if estado == True:
           print("Hola")

2. Errores de excepción (Exceptions)
   Ocurren durante la ejecución del programa.
"""

# ==================================================
#           EJEMPLO 02: INDEX ERROR
# ==================================================

def ejemplo_exception_002():
    lista_numeros = [1, "Python", 3, True, 5]

    try:
        indice_ingresado = int(input("Ingrese el índice: "))
        elemento_mostrar = lista_numeros[indice_ingresado]
        print(f"El valor mostrado es: {elemento_mostrar}")
    except IndexError:
        print("Error: el índice está fuera del rango de la lista.\n")
    except ValueError:
        print("Error: debe ingresar un número entero.\n")

# ==================================================
#           EJEMPLO 03: ERRORES ESPECÍFICOS
# ==================================================

def ejemplo_exception_003():
    try:
        x = int(input("Introduzca un número entero: "))
        y = 10 / x
        print(f"Resultado: {y}")
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.")
    except ValueError:
        print("Error: debe introducir un número entero válido.")
    else:
        print("Operación realizada correctamente.")
    finally:
        print("Fin del ejemplo.\n")

# ==================================================
#               EJECUCIÓN DE EJEMPLOS
# ==================================================

# ejemplo_exception_001()
# ejemplo_exception_002()
# ejemplo_exception_003()