import os
import keyboard

from functools import reduce

def cargar_laberinto():
    laberinto = []
    with open("C:/Users/david/Documents/ejercicios python/proyecto original/Proyecto-original/mapas/laberinto.txt", "r") as archivo:
        lineas = archivo.readlines()[4:]  # Leer todas las líneas después de las primeras cuatro
        for linea in lineas:
            laberinto.append(list(linea.strip()))
    return laberinto

def mostrar_fila(fila):
    return " ".join(fila)

def mostrar_laberinto(laberinto, jugador_x, jugador_y):
    os.system("cls" if os.name == "nt" else "clear")
    
    # Agregar al jugador en las coordenadas proporcionadas
    laberinto_con_jugador = [list(fila) for fila in laberinto]
    laberinto_con_jugador[jugador_y][jugador_x] = "P"
    
    # Imprimir el laberinto con las coordenadas del jugador
    for fila in laberinto_con_jugador:
        fila_str = " ".join(fila)
        print(fila_str)
    
    # Mostrar las coordenadas del jugador
    print(f"Coordenadas del jugador: ({jugador_x}, {jugador_y})")

    # Añadir espacios en blanco para mantener el formato 20x20
    espacios_en_blanco = " " * (20 - len(laberinto[0]))
    for _ in range(20 - len(laberinto)):
        print(espacios_en_blanco)



def mover_jugador(laberinto, direccion, jugador_x, jugador_y):
    nuevo_x, nuevo_y = jugador_x, jugador_y

    if direccion == "up" and jugador_y > 0 and laberinto[jugador_y - 1][jugador_x] != "#":
        nuevo_y -= 1
    elif direccion == "down" and jugador_y < len(laberinto) - 1 and laberinto[jugador_y + 1][jugador_x] != "#":
        nuevo_y += 1
    elif direccion == "left" and jugador_x > 0 and laberinto[jugador_y][jugador_x - 1] != "#":
        nuevo_x -= 1
    elif direccion == "right" and jugador_x < len(laberinto[0]) - 1 and laberinto[jugador_y][jugador_x + 1] != "#":
        nuevo_x += 1

    if laberinto[nuevo_y][nuevo_x] == "F":
        return None, None  # El jugador llegó a la salida

    return nuevo_x, nuevo_y

def main():
    nombre_jugador = input("Ingrese su nombre: ")
    print(f"Bienvenido, {nombre_jugador}!")
    input("Presiona Enter para comenzar...")
    
    laberinto = cargar_laberinto()
    jugador_x, jugador_y = None, None
    
    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            if laberinto[i][j] == "P":
                jugador_x, jugador_y = j, i
    
    while True:
        mostrar_laberinto(laberinto, jugador_x, jugador_y)
        tecla = keyboard.read_event().name

        if tecla in ["up", "down", "left", "right"]:
            nuevo_x, nuevo_y = mover_jugador(laberinto, tecla, jugador_x, jugador_y)

            if nuevo_x is not None and nuevo_y is not None:
                laberinto[jugador_y][jugador_x] = "."
                jugador_x, jugador_y = nuevo_x, nuevo_y
                laberinto[jugador_y][jugador_x] = "P"
            else:
                print("¡Has llegado a la salida!")
                break
        elif tecla == "enter":
            break

if __name__ == "__main__":
    main()
