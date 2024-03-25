import funciones_funcionalidad
import time


def iniciar_juego():
    print("Bienvenido al Trivial!\nPor favor, indique qué quiere hacer:")
    print("1. Modo normal")
    print("2. Modo 'Quién quiere ser millonario'")
    print("3. Modo carrera")
    print("4. Estadísticas personales")
    print("\n")
    respuesta = int(input("Selecciona una opción (introduce el número): "))
    return respuesta

def iniciar_modo_carrera():
    print("Vas a jugar al modo carrera. Este modo de juego consiste en acertar todas las preguntas que puedas sobre un tema en específico. Tú eliges el tema y la dificultad. Tienes tres vidas.")
    dificultad = funciones_funcionalidad.seleccion_dificultad()
    categoria = funciones_funcionalidad.seleccion_categoria()
    vidas = 3
    aciertos = 0
    contador = 1
    while vidas > 0:
        print(f"Tienes {vidas} vidas")
        if funciones_funcionalidad.jugar_modo_carrera(contador, 1, categoria, dificultad) == 1:
            aciertos = aciertos + 1

        else:
            vidas = vidas - 1
        contador = contador + 1
    print("¡Te has quedado sin vidas!")
    print(f"Has acertado {aciertos} preguntas de la categoría {categoria}")


def get_num_preguntas():
    print("Bienvenido al Trivial! Por favor, inserte el número de preguntas que quieres jugar: ")
    num_preguntas = int(input("Introduce un número: "))
    return num_preguntas

#iniciar_modo_carrera()