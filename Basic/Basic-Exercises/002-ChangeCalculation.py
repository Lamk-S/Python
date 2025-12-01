"""
Descripción
-----------
Calcular el cambio correspondiente a una transacción, desglosándolo
en billetes y monedas de diferentes denominaciones.

El programa:
1. Calcula el cambio total.
2. Desglosa el cambio en billetes y monedas.
"""


def calcula_cambio(costo: float, pagado: float) -> dict:
    # Paso 1: calcular el cambio total
    cambio = pagado - costo

    # Paso 2: desglosar el cambio en billetes y monedas
    denominaciones = [100, 50, 20, 10, 5, 1, 0.5, 0.25, 0.1, 0.05, 0.01]
    desglose = {}

    for valor in denominaciones:
        cantidad = int(cambio // valor)
        cambio = round(cambio % valor, 2)  # evitar errores de punto flotante

        if cantidad > 0:
            desglose[valor] = cantidad

    return desglose

# -----------------------------
# Ejemplo de uso
# -----------------------------
 
costo = 23.75
pagado = 50

print("Desglose del cambio:")
resultado = calcula_cambio(costo, pagado)

for den, cant in resultado.items():
    print(f"{den}: {cant}")