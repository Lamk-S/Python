# ===========================================
#  Módulo Matemático (math)
# ===========================================
import math
print(math.pi)
print(math.sqrt(16))

# ===========================================
#  Módulo de Estadísticas (statistics)
# ===========================================
import statistics
datos = [2.90, 3.75, 4.10, 5.25, 6.80]
media = statistics.mean(datos)
mediana = statistics.median(datos)
moda = statistics.mode(datos)
print(f"Media: {media} - Mediana: {mediana} - Moda: {moda}")

# ===========================================
# Módulo de Números Aleatorios (random)
# ===========================================
import random
numeros_azar = random.randint(1, 100)
print(f"Número aleatorio entre 1 y 100: {numeros_azar}")

cursos = ['Python', 'JavaScript', 'Java', 'C#', 'Ruby']
estudiar_mes = random.choice(cursos)
print(f"Curso seleccionado para estudiar este mes: {estudiar_mes}")

# ===========================================
# Módulo de Fechas y Tiempos (datetime)
# ===========================================
from datetime import datetime, timedelta
fecha_actual = datetime.now()
print(f"Fecha y hora actual: {fecha_actual}")

# Formatear fecha y extraer componentes
fecha_formateada = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")
print(f"Fecha formateada: {fecha_formateada}")
print(f"Año: {fecha_actual.year}, Mes: {fecha_actual.month}, Día: {fecha_actual.day}")
print(f"Hora: {fecha_actual.hour}, Minuto: {fecha_actual.minute}, Segundo: {fecha_actual.second}")

# Operaciones con fechas
nueva_fecha = fecha_actual + timedelta(days=7)
print(f"Fecha dentro de 7 días: {nueva_fecha.strftime("%Y-%m-%d %H:%M:%S")}")

fecha1 = datetime(2025, 5, 10)
fecha2 = datetime(2025, 3, 15)
diferencia_entre_fechas = fecha1 - fecha2
print(f"Diferencia entre días: {diferencia_entre_fechas.days} días")