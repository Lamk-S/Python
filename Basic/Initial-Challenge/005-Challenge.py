# =====================================================
# 005.- Convertir segundos a horas, minutos y segundos
# =====================================================

total_segundos = int(input("Ingrese la cantidad de segundos: "))
total_horas = total_segundos // 3600
minutos = (total_segundos % 3600) // 60
segundos_rest = total_segundos % 60
print(f"{total_horas}h, {minutos}min, {segundos_rest}s")