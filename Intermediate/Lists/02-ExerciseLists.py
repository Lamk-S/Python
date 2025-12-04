# ---------------------------------------------------------
# Ejercicio: Operaciones básicas con listas en Python
# ---------------------------------------------------------

# Creación de una lista vacía para almacenar frutas
frutas = list()

# ---------------------------------------------------------
# Ingreso de elementos a la lista "frutas"
# Restricción: no se permiten elementos repetidos
# ---------------------------------------------------------

while True:
    nueva_fruta = input("Ingrese la fruta: ")

    # Verificar si la fruta ya existe en la lista
    if nueva_fruta in frutas:
        posicion = frutas.index(nueva_fruta)
        print(f"La fruta ya existe y se encuentra en la posición {posicion}")

        rpta = input("¿Desea continuar? (s/n): ")
        if rpta.lower() == "n":
            break
    else:
        frutas.append(nueva_fruta)
        print(frutas)

# ---------------------------------------------------------
# Enumeración de elementos de una lista
# ---------------------------------------------------------

# Lista de ejemplo
frutas = ["manzana", "banana", "naranja", "kiwi"]

# enumerate() permite obtener índice y valor al mismo tiempo
# start=1 hace que la numeración comience en 1 en lugar de 0
for index, nombre in enumerate(frutas, start=1):
    print(f"{index} {nombre}")