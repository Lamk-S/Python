"""
Descripción:
Ejemplos básicos del uso de la librería Colorama para aplicar colores,
fondos y estilos al texto en programas de consola.
"""

from colorama import Fore, Back, Style, init

# Inicializar Colorama para que funcione correctamente en todas las plataformas
init(autoreset=True)


# ==========================================
#        EJEMPLOS DE USO DE COLORAMA
# ==========================================

def ejemplo_uso_colorama():
    """
    Muestra ejemplos básicos de cómo aplicar colores, fondos
    y estilos utilizando la librería Colorama.
    """

    print(Fore.RED + "Este es un texto en rojo")
    print(Back.GREEN + "Este texto tiene un fondo verde")
    print(Fore.YELLOW + Back.BLUE + "Texto amarillo con fondo azul")
    print(Style.BRIGHT + "Texto en negrita (BRIGHT)")
    print(Fore.WHITE + Back.BLACK +
          "Texto blanco sobre fondo negro" +
          Style.RESET_ALL)


# ==========================================
#               MENÚ CON COLORES
# ==========================================

def menu_opciones():
    icono_opcion_1 = "\U0001F4C8"  # Gráfico de barras
    icono_opcion_2 = "\U0001F4B0"  # Símbolo de dinero
    icono_opcion_3 = "\U0001F4DA"  # Libros

    borde_superior = f"{Fore.YELLOW}{Back.BLUE}+" + "-" * 30 + "+"
    borde_inferior = f"{Fore.YELLOW}{Back.BLUE}+" + "-" * 30 + "+"

    opciones = [
        f"{Fore.CYAN}{Back.BLACK}| 1. Opción 1 {icono_opcion_1}               |",
        f"{Fore.CYAN}{Back.BLACK}| 2. Opción 2 {icono_opcion_2}               |",
        f"{Fore.CYAN}{Back.BLACK}| 3. Opción 3 {icono_opcion_3}               |"
    ]

    print(borde_superior)
    for opcion in opciones:
        print(opcion)
    print(borde_inferior)


# ==========================================
#              EJECUCIÓN DE USO
# ==========================================

menu_opciones()

try:
    seleccion = int(input(f"{Fore.GREEN}Seleccione una opción: "))
except ValueError:
    print(f"{Fore.RED}Entrada inválida. Debe ingresar un número.")
    exit()

if seleccion == 1:
    print(f"{Fore.GREEN}Has seleccionado la Opción 1")
elif seleccion == 2:
    print(f"{Fore.GREEN}Has seleccionado la Opción 2")
elif seleccion == 3:
    print(f"{Fore.GREEN}Has seleccionado la Opción 3")
else:
    print(f"{Fore.RED}Opción no válida. Inténtalo de nuevo.")