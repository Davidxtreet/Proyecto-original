import os
import keyboard

def cargar_laberinto():
    laberinto = []
    with open("C:/Users/david/Documents/ejercicios python/proyecto original/Proyecto-original/mapas/laberinto.txt", "r") as archivo:
        for i, linea in enumerate(archivo):
            if i < 4:
                continue  # Saltar las primeras cuatro filas
            laberinto.append(list(linea.strip()))
    return laberinto

def mostrar_laberinto(laberinto):
    os.system("cls" if os.name == "nt" else "clear")
    for fila in laberinto:
        print(" ".join(fila))

def mover_jugador(laberinto, direccion, jugador):
    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            if laberinto[i][j] == jugador:
                if direccion == "arriba" and i > 0 and laberinto[i - 1][j] != "#":
                    laberinto[i][j] = "."
                    laberinto[i - 1][j] = jugador
                    return
                elif direccion == "abajo" and i < len(laberinto) - 1 and laberinto[i + 1][j] != "#":
                    laberinto[i][j] = "."
                    laberinto[i + 1][j] = jugador
                    return
                elif direccion == "izquierda" and j > 0 and laberinto[i][j - 1] != "#":
                    laberinto[i][j] = "."
                    laberinto[i][j - 1] = jugador
                    return
                elif direccion == "derecha" and j < len(laberinto[i]) - 1 and laberinto[i][j + 1] != "#":
                    laberinto[i][j] = "."
                    laberinto[i][j + 1] = jugador
                    return

def main():
    nombre_jugador = input("Ingrese su nombre: ")
    print(f"Bienvenido, {nombre_jugador}!")
    input("Presiona Enter para comenzar...")
    
    laberinto = cargar_laberinto()
    jugador = "P"
    mostrar_laberinto(laberinto)
    
    while True:
        tecla = keyboard.read_event().name
        if tecla == "up":
            mover_jugador(laberinto, "arriba", jugador)
        elif tecla == "down":
            mover_jugador(laberinto, "abajo", jugador)
        elif tecla == "left":
            mover_jugador(laberinto, "izquierda", jugador)
        elif tecla == "right":
            mover_jugador(laberinto, "derecha", jugador)
        elif tecla == "enter":
            break
        
        mostrar_laberinto(laberinto)

    print("¡Has salido del laberinto!")
    
if __name__ == "__main__":
    main()

