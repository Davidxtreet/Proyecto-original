# Proyecto Integrador parte 1
import keyboard
print("Ingrese el nombre de su jugador:")
nombre = input()
print("Bienvenido ", nombre, " es un placer, escapa! si es que puedes.")

# Proyecto Integrador parte 2


# bucle infinito leyendo e imprimiento las teclas y sólo terminará cuando se presione la tecla ↑


def main():
    print("El programa está corriendo. Presiona la tecla ↑ para terminar.")
    while True:
        tecla = keyboard.read_event(suppress=True).name
        print("Tecla ingresada:", tecla)
        if tecla == 'up':
            print("Terminando el bucle...")
            break


if __name__ == "__main__":
    main()

#proyecto Integrador parte 3

import os

def borrar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def bucle_principal():
    numero = 0
    while numero <= 50:
        borrar_terminal()
        print(f"Número actual: {numero}")

        tecla = input("Presiona 'n' para continuar (o cualquier otra tecla para salir): ")
        if tecla.lower() == 'n':
            numero += 1
        else:
            break

if __name__ == "__main__":
    bucle_principal()

#proyecto integrador parte 4

import os
import keyboard

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_map(game_map):
    for row in game_map:
        print(''.join(row))
    print()

def main_loop(game_map, start_pos, end_pos):
    px, py = start_pos
    
    while (px, py) != end_pos:
        game_map[py][px] = 'P'
        clear_screen()
        display_map(game_map)
        game_map[py][px] = '.'
        
        key = keyboard.read_event().name
        
        if key == 'up':
            new_px, new_py = px, py - 1
        elif key == 'down':
            new_px, new_py = px, py + 1
        elif key == 'left':
            new_px, new_py = px - 1, py
        elif key == 'right':
            new_px, new_py = px + 1, py
        else:
            continue
        
        if (
            0 <= new_px < len(game_map[0]) and
            0 <= new_py < len(game_map) and
            game_map[new_py][new_px] != '#'
        ):
            px, py = new_px, new_py

    clear_screen()
    display_map(game_map)
    print("¡Has llegado al final!")

# Mapa del laberinto en forma de cadena
maze_str = """
#.###################
#.#.....#...#.....#.#
#.#.#####.#.###.#.#.#
#.#...#.#.#...#.#...#
#.#.#.#.###.#####.###
#...#...#.#.#.#...#.#
#.#.###.#.#.#.###.#.#
#.#.#.......#.#.....#
#######.#.###.#.#.#.#
#.......#...#...#.#.#
#.#####.###########.#
#.#...#.......#.....#
#.#.###.#####.#.#.###
#.....#.#.......#...#
#.#######.#######.###
#.#.....#.#...#.....#
###.###.#.#.###.#####
#...#...#.....#...#.#
#.#.#.#####.#.###.#.#
#.#.#.......#...#...#
###################.#

"""

# Convertir la cadena en una matriz de caracteres
maze_lines = maze_str.strip().split("\n")
game_map = [list(line) for line in maze_lines]

# Definir posiciones inicial y final
start_position = (1, 0)
end_position = (len(game_map[0]) - 1, len(game_map) - 1)

main_loop(game_map, start_position, end_position)

