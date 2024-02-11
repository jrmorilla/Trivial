import funciones_preguntas
import funciones_sqlite
import inicializacion

def jugar_modo_normal(num_preguntas):
    json_raw = funciones_preguntas.get_json_raw(num_preguntas)
    contador = 1
    puntuacion = 0
    for i in json_raw:
        if funciones_sqlite.comprobar_existencia_pregunta_DB(funciones_preguntas.sacar_pregunta(i)) == False:
            funciones_sqlite.añadir_datos_pregunta(PREGUNTA=funciones_preguntas.sacar_pregunta(i),
                                                   RESPUESTAS=funciones_preguntas.get_respuestas(i),
                                                   RESPUESTA_CORRECTA=funciones_preguntas.respuesta_correcta(i),
                                                   TOPIC=funciones_preguntas.get_topic(i),
                                                   DIFICULTAD=funciones_preguntas.get_difficulty(i))
        else:
            pass
        print(f"Tu puntuación es: {puntuacion} puntos")
        print("\n")
        opciones = funciones_preguntas.construir_opciones_enumeradas(i)
        print(f"Pregunta {contador}: {funciones_preguntas.sacar_pregunta(i)}")
        for indice, elemento in enumerate(opciones):
            print(f"{indice + 1}. {elemento}")
        print("\n")
        respuesta = int(input("Elige un número: "))
        if funciones_preguntas.determinar_acierto(i, opciones, respuesta):
            funciones_sqlite.añadir_datos_estadistica(TOPIC = funciones_preguntas.get_topic(i),
                                                      DIFICULTAD = funciones_preguntas.get_difficulty(i),
                                                      EVALUACION = 1)
            puntuacion = puntuacion + 1
        else:
            funciones_sqlite.añadir_datos_estadistica(TOPIC=funciones_preguntas.get_topic(i),
                                                      DIFICULTAD=funciones_preguntas.get_difficulty(i),
                                                      EVALUACION=0)
        contador = contador + 1
    print(f"Has obtenido {puntuacion} puntos")

def jugar_modo_carrera(contador, num_preguntas, categoria, dificultad):
    json_raw = funciones_preguntas.get_json_raw_modo_carrera(1, categoria, dificultad)
    if funciones_sqlite.comprobar_existencia_pregunta_DB(funciones_preguntas.sacar_pregunta(json_raw[0])) == False:
        funciones_sqlite.añadir_datos_pregunta(PREGUNTA = funciones_preguntas.sacar_pregunta(json_raw[0]),
                                               RESPUESTAS = funciones_preguntas.get_respuestas(json_raw[0]),
                                               RESPUESTA_CORRECTA = funciones_preguntas.respuesta_correcta(json_raw[0]),
                                               TOPIC = funciones_preguntas.get_topic(json_raw[0]),
                                               DIFICULTAD = funciones_preguntas.get_difficulty(json_raw[0]))
    else:
        pass
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