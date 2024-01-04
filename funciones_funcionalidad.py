import funciones_preguntas
import inicializacion

def jugar_modo_normal(num_preguntas):
    json_raw = funciones_preguntas.get_json_raw(num_preguntas)
    contador = 1
    puntuacion = 0
    for i in json_raw:
        print(f"Tu puntuación es: {puntuacion} puntos")
        print("\n")
        opciones = funciones_preguntas.construir_opciones_enumeradas(i)
        print(f"Pregunta {contador}: {funciones_preguntas.sacar_pregunta(i)}")
        for indice, elemento in enumerate(opciones):
            print(f"{indice + 1}. {elemento}")
        print("\n")
        respuesta = int(input("Elige un número: "))
        if funciones_preguntas.determinar_acierto(i, opciones, respuesta):
            puntuacion = puntuacion + 1
        contador = contador + 1
    print(f"Has obtenido {puntuacion} puntos")

def jugar_modo_carrera(num_preguntas, categoria, dificultad):
    json_raw = funciones_preguntas.get_json_raw_modo_carrera(num_preguntas, categoria, dificultad)
    contador = 1
    puntuacion = 0
    for i in json_raw:
        print(f"Tu puntuación es: {puntuacion} puntos")
        print("\n")
        opciones = funciones_preguntas.construir_opciones_enumeradas(i)
        print(f"Pregunta {contador}: {funciones_preguntas.sacar_pregunta(i)}")
        for indice, elemento in enumerate(opciones):
            print(f"{indice + 1}. {elemento}")
        print("\n")
        respuesta = int(input("Elige un número: "))
        if funciones_preguntas.determinar_acierto(i, opciones, respuesta):
            puntuacion = puntuacion + 1
        contador = contador + 1
    print(f"Has obtenido {puntuacion} puntos")

jugar_modo_carrera(10, 3, 'easy')