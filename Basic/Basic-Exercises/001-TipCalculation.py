"""
Descripción
-----------
Calcular la propina en un restaurante con base en:
- El total de la cuenta
- El porcentaje de propina a aplicar

El programa calcula:
1. El monto de la propina
2. El total a pagar (cuenta + propina)
"""


def calcular_propina(total_cuenta: float, porcentaje_propina: float) -> tuple:
    propina = total_cuenta * (porcentaje_propina / 100)
    total_a_pagar = total_cuenta + propina
    return propina, total_a_pagar


total_cuenta = 100
porcentaje_propina = 15

propina, total_a_pagar = calcular_propina(total_cuenta, porcentaje_propina)

print(f"La propina es: ${propina:.2f}")
print(f"Total a pagar: ${total_a_pagar:.2f}")