"""
Descripción:
Juego básico de "Piedra, Papel o Tijera" en Python.
El jugador compite contra la computadora y se lleva un registro
de las victorias de ambos hasta que el usuario decida terminar la partida.
"""

import random


# ==========================================
#     FUNCIÓN PARA JUGAR UNA SOLA RONDA
# ==========================================

def jugar(victorias_jugador, victorias_computadora):
    opciones = ["piedra", "papel", "tijera"]

    jugador = input("Elige: piedra, papel o tijera: ").lower()

    # Validación de la elección del jugador
    if jugador not in opciones:
        print("Opción no válida. Debes elegir: piedra, papel o tijera.")
        return victorias_jugador, victorias_computadora

    # Elección aleatoria de la computadora
    computadora = random.choice(opciones)

    print(f"Tu elegiste: {jugador}")
    print(f"La computadora eligió: {computadora}")

    # Determinar el resultado
    if jugador == computadora:
        print("Es un empate.")
    elif (
        (jugador == "piedra" and computadora == "tijera") or
        (jugador == "papel" and computadora == "piedra") or
        (jugador == "tijera" and computadora == "papel")
    ):
        print("¡Ganaste!")
        victorias_jugador += 1
    else:
        print("¡Perdiste!")
        victorias_computadora += 1

    return victorias_jugador, victorias_computadora


# ==========================================
#     BUCLE PRINCIPAL DEL JUEGO
# ==========================================

def juego_piedra_papel_tijera():
    """
    Función principal que gestiona el ciclo del juego.
    Permite jugar múltiples rondas y muestra estadísticas al final.
    """

    print("Bienvenido al juego de Piedra, Papel o Tijera")

    victorias_jugador = 0
    victorias_computadora = 0

    while True:
        victorias_jugador, victorias_computadora = jugar(
            victorias_jugador,
            victorias_computadora
        )

        jugar_otra_vez = input("¿Quieres jugar otra vez? (SI/NO): ").lower()

        if jugar_otra_vez != "si":
            print("\n-- Estadísticas Finales --")
            print(f"Victorias del jugador: {victorias_jugador}")
            print(f"Victorias de la computadora: {victorias_computadora}")

            if victorias_jugador > victorias_computadora:
                print("¡Felicidades! Ganaste más veces.")
            elif victorias_jugador < victorias_computadora:
                print("La computadora ganó más rondas. ¡Sigue intentando!")
            else:
                print("El juego terminó en un empate total.")

            print("Gracias por jugar.")
            break


# ==========================================
#           EJECUCIÓN DEL JUEGO
# ==========================================

juego_piedra_papel_tijera()