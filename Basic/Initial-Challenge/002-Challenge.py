# =====================================================
# 002.- Calcular el salario semanal
# =====================================================

nombre_trabajador = input("Ingrese el nombre del trabajdor: ")
horas_trab = int(input("Ingrese las horas trabajadas: "))
tarifa_hora = float(input("Ingrese la tarifa por hora: "))
salario_diario = tarifa_hora * horas_trab
print(f"El salio del trabajador {nombre_trabajador} es {salario_diario}")