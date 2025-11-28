"""
Asignación de calificaciones según nota:

Nota >= 90            : A
80 <= Nota < 90       : B
70 <= Nota < 80       : C
60 <= Nota < 70       : D
Nota < 60             : F
"""

nota = int(input("Introduce la nota del estudiante: "))

if nota >= 90:
    print("Calificación A")
elif nota >= 80:
    print("Calificación B")
elif nota >= 70:
    print("Calificación C")
elif nota >= 60:
    print("Calificación D")
else:
    print("Calificación F")