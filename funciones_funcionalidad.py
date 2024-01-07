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

def jugar_modo_carrera(contador, num_preguntas, categoria, dificultad):
    json_raw = funciones_preguntas.get_json_raw_modo_carrera(1, categoria, dificultad)
    print("\n")
    opciones = funciones_preguntas.construir_opciones_enumeradas(json_raw[0])
    print(f"Pregunta {contador}: {funciones_preguntas.sacar_pregunta(json_raw[0])}")
    for indice, elemento in enumerate(opciones):
        print(f"{indice + 1}. {elemento}")
    print("\n")
    respuesta = int(input("Elige un número: "))
    if funciones_preguntas.determinar_acierto(json_raw[0], opciones, respuesta):
        return 1
    else:
        return 0

def seleccion_categoria():
    categorias = ['Books', 'Film', 'Music', 'Musicals & Theatres', 'Television', 'Video Games', 'Board Games', 'Nature',
                  'Computers', 'Mathematics', 'Mythology', 'Sport', 'Geography', 'History', 'Politics', 'Art', 'Celebrities',
                  'Animals', 'Vehicles', 'Comics', 'Gadgets', 'Anime & Manga', 'Cartoon & Animations']
    print("Categoría existentes: ")
    for indice, categoria in enumerate(categorias):
        print(f"{indice + 1}. {categoria}")
    print("\n")
    eleccion = int(input("Introduce el número de una categoría: "))
    return eleccion + 9

def seleccion_dificultad():
    dificultades = ['easy', 'medium', 'hard']
    print("Selecciona la dificultad:")
    for indice, dificultad in enumerate(dificultades):
        print(f"{indice + 1}. {dificultad}")
    eleccion = int(input("Introduce el número de una dificultad: "))
    return dificultades[eleccion -1]

def seleccion_num_preguntas():
    num_preguntas = int(input("Introduce cuántas preguntas tendrá esta partida: "))
    return num_preguntas