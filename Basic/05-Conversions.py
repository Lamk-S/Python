# ==========================================
#     DECLARACIÓN DE VARIABLES BÁSICAS
# ==========================================

nombre_per = "Melvin"
apellido_per = "López"
edad_per = 24
sueldo_per = 1200.98212
act_per = True               # Estado activo/inactivo (booleano)
total_prod = "1900"          # Cantidad total representada como cadena
cantidad_prod = 8

# ==========================================
#        CONVERSIÓN DE TIPOS DE DATOS
# ==========================================

# Convertimos total_prod (string) a entero para poder operar aritméticamente
total_pagar = int(total_prod) * cantidad_prod
# print(total_pagar)

# Convertimos el sueldo (float) a cadena para fines de visualización o almacenamiento
cadena_dos = str(sueldo_per)
tipo_dato = type(cadena_dos)
# print(tipo_dato)

# ==========================================
#     CONCATENACIÓN Y FORMATO DE STRINGS
# ==========================================

# 1. Concatenación básica (se debe convertir todo a string)
cadena_uno = nombre_per + str(edad_per)

# 2. Concatenación usando comas (print agrega espacios automáticamente)
print(nombre_per, sueldo_per)

# 3. Uso de f-strings (la forma más recomendada y legible)
print(f"El nombre de la persona es {nombre_per} y su sueldo es {round(sueldo_per, 3)}")

# Formateo del sueldo limitando a 2 decimales utilizando f-string
nuevo_sueldo = f"{sueldo_per:.2f}"
print(nuevo_sueldo)