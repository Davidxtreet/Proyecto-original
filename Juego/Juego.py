import os
import keyboard
import random

class Juego:
    def __init__(self, directorio_mapas):
        self.directorio_mapas = directorio_mapas
        self.laberinto = None
        self.jugador_x = None
        self.jugador_y = None

    def cargar_laberinto(self, archivo_mapa):
        with open(archivo_mapa, "r") as archivo:
            lineas = archivo.readlines()[4:]  # Leer todas las líneas después de las primeras cuatro
            self.laberinto = [list(linea.strip()) for linea in lineas]

    def cargar_mapa_aleatorio(self):
        archivos_mapas = os.listdir(self.directorio_mapas)
        archivo_mapa = random.choice(archivos_mapas)
        ruta_mapa = os.path.join(self.directorio_mapas, archivo_mapa)
        return ruta_mapa

    def mostrar_fila(self, fila):
        return " ".join(fila)

    def mostrar_laberinto(self):
        os.system("cls" if os.name == "nt" else "clear")

        # Agregar al jugador en las coordenadas proporcionadas
        laberinto_con_jugador = [list(fila) for fila in self.laberinto]
        laberinto_con_jugador[self.jugador_y][self.jugador_x] = "P"

        # Imprimir el laberinto con las coordenadas del jugador
        for fila in laberinto_con_jugador:
            fila_str = " ".join(fila)
            print(fila_str)

        # Mostrar las coordenadas del jugador
        print(f"Coordenadas del jugador: ({self.jugador_x}, {self.jugador_y})")

        # Añadir espacios en blanco para mantener el formato 20x20
        espacios_en_blanco = " " * (20 - len(self.laberinto[0]))
        for _ in range(20 - len(self.laberinto)):
            print(espacios_en_blanco)

    def mover_jugador(self, direccion):
        nuevo_x, nuevo_y = self.jugador_x, self.jugador_y

        if direccion == "up" and self.jugador_y > 0 and self.laberinto[self.jugador_y - 1][self.jugador_x] != "#":
            nuevo_y -= 1
        elif direccion == "down" and self.jugador_y < len(self.laberinto) - 1 and self.laberinto[self.jugador_y + 1][self.jugador_x] != "#":
            nuevo_y += 1
        elif direccion == "left" and self.jugador_x > 0 and self.laberinto[self.jugador_y][self.jugador_x - 1] != "#":
            nuevo_x -= 1
        elif direccion == "right" and self.jugador_x < len(self.laberinto[0]) - 1 and self.laberinto[self.jugador_y][self.jugador_x + 1] != "#":
            nuevo_x += 1

        if self.laberinto[nuevo_y][nuevo_x] == "F":
            return None, None  # El jugador llegó a la salida

        return nuevo_x, nuevo_y

    def ejecutar_juego(self):
        nombre_jugador = input("Ingrese su nombre: ")
        print(f"Bienvenido, {nombre_jugador}!")
        input("Presiona Enter para comenzar...")

        ruta_mapa_aleatorio = self.cargar_mapa_aleatorio()
        self.cargar_laberinto(ruta_mapa_aleatorio)

        for i in range(len(self.laberinto)):
            for j in range(len(self.laberinto[i])):
                if self.laberinto[i][j] == "P":
                    self.jugador_x, self.jugador_y = j, i

        while True:
            self.mostrar_laberinto()
            tecla = keyboard.read_event().name

            if tecla in ["up", "down", "left", "right"]:
                nuevo_x, nuevo_y = self.mover_jugador(tecla)

                if nuevo_x is not None and nuevo_y is not None:
                    self.laberinto[self.jugador_y][self.jugador_x] = "."
                    self.jugador_x, self.jugador_y = nuevo_x, nuevo_y
                    self.laberinto[self.jugador_y][self.jugador_x] = "P"
                else:
                    print("¡Has llegado a la salida!")
                    break
            elif tecla == "enter":
                break

if __name__ == "__main__":
    directorio_mapas = "C:/Users/david/Documents/ejercicios python/proyecto original/Proyecto-original/mapas"
    juego = Juego(directorio_mapas)
    juego.ejecutar_juego()
