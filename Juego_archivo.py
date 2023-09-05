import os
import keyboard

class JuegoLaberinto:
    def __init__(self):
        self.nombre_jugador = ""
        self.laberinto = []
        self.jugador = "P"

    def cargar_laberinto(self, archivo_path):
        with open(archivo_path, "r") as archivo:
            for i, linea in enumerate(archivo):
                if i < 4:
                    continue  # Saltar las primeras cuatro filas
                self.laberinto.append(list(linea.strip()))

    def mostrar_laberinto(self):
        os.system("cls" if os.name == "nt" else "clear")
        for fila in self.laberinto:
            print(" ".join(fila))

    def mover_jugador(self, direccion):
        for i in range(len(self.laberinto)):
            for j in range(len(self.laberinto[i])):
                if self.laberinto[i][j] == self.jugador:
                    if direccion == "arriba" and i > 0 and self.laberinto[i - 1][j] != "#":
                        self.laberinto[i][j] = "."
                        self.laberinto[i - 1][j] = self.jugador
                        return
                    elif direccion == "abajo" and i < len(self.laberinto) - 1 and self.laberinto[i + 1][j] != "#":
                        self.laberinto[i][j] = "."
                        self.laberinto[i + 1][j] = self.jugador
                        return
                    elif direccion == "izquierda" and j > 0 and self.laberinto[i][j - 1] != "#":
                        self.laberinto[i][j] = "."
                        self.laberinto[i][j - 1] = self.jugador
                        return
                    elif direccion == "derecha" and j < len(self.laberinto[i]) - 1 and self.laberinto[i][j + 1] != "#":
                        self.laberinto[i][j] = "."
                        self.laberinto[i][j + 1] = self.jugador
                        return

    def jugar(self, archivo_path):
        self.nombre_jugador = input("Ingrese su nombre: ")
        print(f"Bienvenido, {self.nombre_jugador}!")
        input("Presiona Enter para comenzar...")

        self.cargar_laberinto(archivo_path)
        self.mostrar_laberinto()

        while True:
            tecla = keyboard.read_event().name
            if tecla == "up":
                self.mover_jugador("arriba")
            elif tecla == "down":
                self.mover_jugador("abajo")
            elif tecla == "left":
                self.mover_jugador("izquierda")
            elif tecla == "right":
                self.mover_jugador("derecha")
            elif tecla == "enter":
                break

            self.mostrar_laberinto()

        print("¡Has salido del laberinto!")

if __name__ == "__main__":
    juego = JuegoLaberinto()
    juego.jugar("C:/Users/david/Documents/ejercicios python/proyecto original/Proyecto-original/mapas/laberinto.txt")




