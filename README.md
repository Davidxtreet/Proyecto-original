nombre_proyecto = "Sal si puedes."
Este es un videojuego de texto de recorrer laberintos. En donde estan representados por caracteres ASCII dónde # representará una pared, . un pasillo y P el personaje. Podrás moverte por el mapa usando las teclas ↑ ↓ ← → de tu teclado.


voy a explicar mi  código paso a paso:

1.  import os
    import keyboard

    from functools import reduce

    En esta sección, importo las bibliotecas necesarias para mi programa. "os" se utiliza para realizar operaciones específicas del sistema operativo, como borrar la pantalla de la consola. "keyboard" es una biblioteca que te permite leer eventos del teclado. "functools" se utiliza para la función, "reduce" que se utiliza más adelante en el código.

2. def cargar_laberinto():
    laberinto = []
    with open("C:/Users/david/Documents/ejercicios python/proyecto original/Proyecto-original/mapas/laberinto.txt", "r") as archivo:
        lineas = archivo.readlines()[4:]  # Leer todas las líneas después de las primeras cuatro
        for linea in lineas:
            laberinto.append(list(linea.strip()))
    return laberinto

    La función "cargar_laberinto" se encarga de cargar el laberinto desde un archivo de texto. Se utiliza un bucle "for" para leer las líneas del archivo después de las primeras cuatro líneas (las cuales son las especificaciones de mi laberinto). Luego, convierte cada línea en una lista de caracteres y la agrega a la lista laberinto. Finalmente, devuelve la lista que representa el laberinto.

3. def mostrar_fila(fila):
    return " ".join(fila)

    "mostrar_fila" es una función simple que toma una lista de caracteres (una fila del laberinto) y la convierte en una cadena, separando cada carácter por un espacio.

4. def mostrar_laberinto(laberinto, jugador_x, jugador_y):
    os.system("cls" if os.name == "nt" else "clear")

    "mostrar_laberinto" es la función encargada de mostrar el laberinto en la consola. Utiliza "os.system" para borrar la pantalla de la consola, dependiendo del sistema operativo.

5.     # Agregar al jugador en las coordenadas proporcionadas
    laberinto_con_jugador = [list(fila) for fila in laberinto]
    laberinto_con_jugador[jugador_y][jugador_x] = "P"

    Aquí se crea una copia del laberinto llamada "laberinto_con_jugador". Luego, se coloca una "P" en las coordenadas del jugador en esta copia, para mostrar la posición actual del jugador.

6.     # Imprimir el laberinto con las coordenadas del jugador
    for fila in laberinto_con_jugador:
        fila_str = " ".join(fila)
        print(fila_str)

    Este bucle "for" recorre cada fila en el laberinto con el jugador y la imprime en la consola como una cadena.

7.     # Mostrar las coordenadas del jugador
    print(f"Coordenadas del jugador: ({jugador_x}, {jugador_y})")

    Esta línea imprime las coordenadas actuales del jugador en la consola.

8.     # Añadir espacios en blanco para mantener el formato 20x20
    espacios_en_blanco = " " * (20 - len(laberinto[0]))
    for _ in range(20 - len(laberinto)):
        print(espacios_en_blanco)

    Estas líneas añaden espacios en blanco al final del laberinto para que tenga un tamaño de 20x20. Calcula la diferencia entre la longitud actual del laberinto y 20, y luego agrega esa cantidad de espacios en blanco en una serie de líneas vacías para mantener la forma del laberinto.

9. def mover_jugador(laberinto, direccion, jugador_x, jugador_y):
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

    "mover_jugador" es la función que controla el movimiento del jugador en el laberinto. Recibe como argumentos el laberinto actual, la dirección en la que el jugador quiere moverse (arriba, abajo, izquierda o derecha), y las coordenadas actuales del jugador (jugador_x y jugador_y).

    Las variables "nuevo_x" y "nuevo_y" se inicializan con las coordenadas actuales del jugador.

    Luego, se verifica la dirección en la que el jugador quiere moverse y se comprueba si ese movimiento es válido (es decir, si no se encuentra en una pared, representada por el carácter #). Si el movimiento es válido, se actualizan las coordenadas "nuevo_x" y "nuevo_y" de acuerdo con la dirección seleccionada.

    Después de mover al jugador, se verifica si el jugador ha llegado a la salida ("F" en el laberinto). Si es así, la función devuelve "None, None", lo que indica que el jugador ha llegado a la salida.

    En caso contrario, la función devuelve las nuevas coordenadas "nuevo_x" y "nuevo_y" después de mover al jugador.

10. while True:
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

    El juego se ejecuta en un bucle "while" "True", que continuará hasta que el jugador llegue a la salida o presione "Enter" para salir del juego.

    En cada iteración del bucle, se llama a "mostrar_laberinto" para mostrar el estado actual del laberinto con la posición del jugador.

    Luego, se espera a que el jugador presione una tecla usando "keyboard.read_event().name". Si la tecla es una de las flechas direccionales (arriba, abajo, izquierda o derecha), se intenta mover al jugador utilizando la función "mover_jugador".

    Si el movimiento es válido, se actualizan las coordenadas del jugador y se marca su posición en el laberinto con un punto ("."). Si el jugador llega a la salida, se imprime un mensaje y el juego se detiene.

    Si el jugador presiona "Enter", el bucle se rompe y el juego termina.

11. if __name__ == "__main__": 

    se utiliza para asegurarse de que el código dentro de ese bloque solo se ejecute cuando el archivo de Python se ejecuta directamente como un programa y no cuando se importa como un módulo en otro script. Esto es una buena práctica en la programación en Python.

Esto es una descripción general de cómo funciona mi código. El programa permite al jugador moverse a través del laberinto y muestra su progreso en la consola.