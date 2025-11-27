# =====================================================
# 004.- Convertir dólares a euros
# =====================================================

cant_dolar = float(input("Ingrese la cantidad de dolares: "))
tipo_cambio = float(input("Ingrese el tipo de cambio: "))
total_euros = cant_dolar * tipo_cambio
print(f"El total de euros es {total_euros:.2f}")