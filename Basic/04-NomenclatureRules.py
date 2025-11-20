"""
REGLAS DE NOMENCLATURA EN PYTHON
--------------------------------

1. Variables y Funciones
    - Estilo: snake_case
    - Los nombres deben ser descriptivos.

    Ejemplos correctos:
       mi_variable = ""
       calcular_suma()

    Ejemplos descriptivos:
       contador_items = ""
       obtener_dato_usuario = ""

2. Constantes
    - Estilo: UPPER_SNAKE_CASE
    - Se usan para valores que no deberían cambiar.

    Ejemplos:
       VALOR_INICIAL = 0
       TIEMPO_MAXIMO = 20


EJEMPLOS CORRECTOS
------------------
precio_total = 150
edad_usuario = 49

nombre_usuario = "Melvin"
apellido_usuario = "López"

def calcular_area(radius):
    return 3.14 * radius ** 2

MAX_CONNECTIONS = 100
PI = 3.14

salario_empleado = 5000
fecha_orden = "20/11/2025"


EJEMPLOS INCORRECTOS
--------------------
pt = 120                        # Nombre no descriptivo
eu = 49                         # Nombre no descriptivo

nombre = "Melvin"               # Ambiguo
def calculararea(radius):       # No usa snake_case
    return 3.14 * radius ** 2

max_connections = 100           # Constante sin UPPERCASE
pi = 3.14                       # Constante sin UPPERCASE

emp_sal = 5000                  # Abreviatura confusa
o_d = "20/11/2025"              # Poco claro
"""