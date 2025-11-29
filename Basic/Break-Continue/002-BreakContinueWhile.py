"""
Uso de Break y Continue en un Bucle WHILE
"""

"""
Ejemplo 1:
Salir del programa cuando el usuario ingrese el número 0.
"""
# while True:
#     numero = int(input("Ingrese un número (0 para salir): "))
#     if numero == 0:
#         print("Saliendo del bucle...")
#         break
#     print(f"Ingresaste: {numero}")

"""
Ejemplo 2:
Solicitar números al usuario, ignorar números negativos usando continue,
e imprimir solo los números positivos. El programa finaliza cuando el usuario ingresa 0.
"""
while True:
    numero = int(input("Introduce un número positivo (0 para salir): "))
    if numero < 0:
        print("Número IGNORADO")
        continue
    if numero == 0:
        print("Saliendo del bucle...")
        break
    print(f"Número válido: {numero}")