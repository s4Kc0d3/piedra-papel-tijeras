# IMPORTS
from random import randint
import time
import os


# ZONA DE FUNCIONES

def banner():
    # Creamos el banner de inicio
    # Limpiamos pantalla
    os.system('cls')
    msg = "Bienvenido al juego (PIEDRA, PAPEL o TIJERA)"
    print("=" * len(msg))
    print(msg)
    print("="*len(msg))
    print("\n")


def piedra_papel_tijera():

    info = {                                                    # Diccionario para traducir el int al string
        1: "piedra",
        2: "papel",
        3: "tijera"
    }

    comments = None                                             # Variable para crear los comentarios
    rounds = int(input("Cuantas rondas vas a jugar? "))         # Número de rondas que se quiere jugar
    actual_round = 1                                            # La ronda actual, siempre es la primera osea 1
    score = {                                                   # Puntuación de la partida
        'jugador': 0,
        'computador': 0
    }

    if rounds == 0:                                             # Si el user introduce 0 es que no quiere jugar
        print("Salimos del juego...")
        exit(0)                                                 # Salimos sin error

    while actual_round <= rounds:
        # Mientras la actual ronda sea menor que la cantidad de rondas deseadas
        # seguiremos en el bucle hasta completar el juego
        print("\nRonda numero:", actual_round, '\n')

        while (True):
            # Para controlar si se pone una opción valida.
            # Se repite hasta que introduce un dato correcto.
            jugada = int(input("Elije: [1]-Piedra, [2]-Papel o [3]-Tijera: "))
            if jugada in info.keys():
                jugada = info[jugada]
                break
            print("No has usado un valor adecuado.")
            time.sleep(0.5)

        # Generamos la jugada de la computadora
        # elegirá un número aleatorio entre 1 y 3 que son las jugadas que se pueden hacer
        computador = info[randint(1,3)]

        if jugada == computador:
            # EN CASO DE EMPATE
            comments = f'Empate en: {jugada}'
            print(comments)
        else:
            if ((jugada == 'piedra' and computador == 'tijera') or
                (jugada == 'tijera' and computador == 'papel') or
                (jugada == 'papel' and computador == 'piedra')):
                # EL JUGADOR GANA
                comments = f'Jugador ganó: {jugada} vs {computador}\n'
                score['jugador'] += 1
                print(comments)
            else:
                # LA MAQUINA GANA
                comments = f'Computadora ganó: {jugada} vs {computador} \n'
                score['computador'] += 1
                print(comments)

        # Damos una pequeña pausa antes que se reinicie la ronda
        time.sleep(0.5)
        # Sumamos 1 en la ronda
        actual_round += 1

    # Cuando se termina la ronda se muestran los resultados
    comments = "Resultado de la partida:"
    print("=" * len(comments))
    print(comments)
    print("="*len(comments))
    print(score,'\n')

if __name__ == "__main__":
    banner()
    piedra_papel_tijera()
