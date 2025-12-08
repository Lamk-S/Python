# Saldo inicial del cajero (variable global)
saldo_cajero = 4000


# -----------------------------------------------------------
# Consultar saldo
# -----------------------------------------------------------
def consultar_saldo():
    print(f"Su saldo actual es: S/.{saldo_cajero}")


# -----------------------------------------------------------
# Retirar dinero
# -----------------------------------------------------------
def retirar_dinero():
    global saldo_cajero
    cantidad = float(input("Ingrese la cantidad a retirar: S/."))
    if cantidad > saldo_cajero:
        print("Fondos insuficientes.")
    else:
        saldo_cajero -= cantidad
        print(f"Ha retirado: S/.{cantidad}. Su nuevo saldo es: S/.{saldo_cajero}")

# -----------------------------------------------------------
# Depositar dinero
# -----------------------------------------------------------
def depositar_dinero():
    global saldo_cajero
    cantidad = float(input("Ingrese la cantidad a depositar: S/."))
    saldo_cajero += cantidad
    print(f"Ha depositado: S/.{cantidad}. Su nuevo saldo es: S/.{saldo_cajero}")
    
# -----------------------------------------------------------
# Mostrar menú
# -----------------------------------------------------------
def mostrar_menu():
    print("\n--- Menú del Cajero Automático ---")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")

# -----------------------------------------------------------
# Bucle principal
# -----------------------------------------------------------
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == '1':
        consultar_saldo()
    elif opcion == '2':
        retirar_dinero()
    elif opcion == '3':
        depositar_dinero()
    elif opcion == '4':
        print("Gracias por usar el cajero automático. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")