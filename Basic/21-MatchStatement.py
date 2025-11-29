"""
Uso de MATCH (Estructura de Patrones)
-------------------------------------
La instrucción `match` en Python permite comparar un valor contra múltiples
patrones, funcionando de forma similar a un "switch" en otros lenguajes.

Sintaxis básica:
match valor:
    case patron1:
        # Acción 1
    case patron2:
        # Acción 2
    case _:
        # Caso por defecto
"""

# Ejemplo tradicional usando if/elif/else
"""
status = input("Ingrese el código status: ")

if status == "200":
    print("Solicitud exitosa")
elif status == "404":
    print("El recurso no fue encontrado")
elif status == "500":
    print("Error interno en el servidor")
else:
    print("Código no existe")
"""

# Ejemplo usando MATCH (forma moderna y más clara)
status = int(input("Ingrese el código de status: "))

match status:
    case 200:
        print("Solicitud exitosa")
    case 404:
        print("El recurso no fue encontrado")
    case 500:
        print("Error interno en el servidor")
    case _:
        print("Código no existe")
