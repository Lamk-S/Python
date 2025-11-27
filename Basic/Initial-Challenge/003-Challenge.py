# =====================================================
# 003.- Calcular el promedio de notas de un alumno
# =====================================================

nota_uno = float(input("Ingrese la nota uno: "))
nota_dos = float(input("Ingrese la nota dos: "))
nota_tres = float(input("Ingrese la tota tres: "))
promedio_final = (nota_uno + nota_dos + nota_tres) / 3

if promedio_final >= 14:
    print(f"El alumno APROBO el curso con promedio {promedio_final}")
else:
    print(f"El alumno DESAPROBO el curso con promedio {promedio_final}")