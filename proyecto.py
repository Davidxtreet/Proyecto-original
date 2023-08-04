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
