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
