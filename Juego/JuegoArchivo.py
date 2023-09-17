from Juego import Juego
import os
import random


class JuegoArchivo(Juego):
    def __init__(self, directorio_mapas):
        self.directorio_mapas = directorio_mapas
        super().__init__(0, 0, 0)

    def cargar_laberinto(self):
        archivo_mapa = self.elegir_mapa_aleatorio()
        super().cargar_laberinto(archivo_mapa)

    def elegir_mapa_aleatorio(self):
        archivos_mapas = os.listdir(self.directorio_mapas)
        archivo_mapa = random.choice(archivos_mapas)
        return os.path.join(self.directorio_mapas, archivo_mapa)
  
if __name__ == "__main__":
    directorio_mapas = "C:/Users/david/Documents/ejercicios python/proyecto original/Proyecto-original/mapas"
    juego = Juego(directorio_mapas)
    juego.ejecutar_juego()  