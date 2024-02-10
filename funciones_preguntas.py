import requests
import random

def get_json_raw_modo_carrera(num_preguntas, categoria, dificultad):
    url = f"https://opentdb.com/api.php?amount={num_preguntas}&category={categoria}&difficulty={dificultad}"

    # Realizar la solicitud HTTP
    respuesta = requests.get(url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if respuesta.status_code == 200:
        # Convertir la respuesta a formato JSON
        datos_json = respuesta.json()

        # Verificar si la solicitud fue exitosa según la propiedad 'response_code'
        if datos_json['response_code'] == 0:
            # Extraer la lista de preguntas
            preguntas = datos_json['results']

            # Devolver la lista de preguntas
            return preguntas
        else:
            print(f"Error en la API. Código de respuesta: {datos_json['response_code']}")
    else:
        print(f"Error al hacer la solicitud. Código de estado: {respuesta.status_code}")

def get_json_raw(cantidad):
    url = f"https://opentdb.com/api.php?amount={cantidad}"

    # Realizar la solicitud HTTP
    respuesta = requests.get(url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if respuesta.status_code == 200:
        # Convertir la respuesta a formato JSON
        datos_json = respuesta.json()

        # Verificar si la solicitud fue exitosa según la propiedad 'response_code'
        if datos_json['response_code'] == 0:
            # Extraer la lista de preguntas
            preguntas = datos_json['results']

            # Devolver la lista de preguntas
            return preguntas
        else:
            print(f"Error en la API. Código de respuesta: {datos_json['response_code']}")
    else:
        print(f"Error al hacer la solicitud. Código de estado: {respuesta.status_code}")

def get_topic(json_raw):
    topic = json_raw['category']
    return topic
def get_difficulty(json_raw):
    difficulty = json_raw['difficulty']
    return difficulty

def sacar_pregunta(json_raw):
    pregunta = json_raw['question']
    return pregunta

def respuesta_correcta(json_raw):
    respuesta_correcta = json_raw['correct_answer']
    return respuesta_correcta
def respuestas_incorrectas(json_raw):
    respuestas_incorrectas = json_raw['incorrect_answers']
    return respuestas_incorrectas

def get_respuestas(json_raw):
    lista= respuestas_incorrectas(json_raw)
    correcta = respuesta_correcta(json_raw)
    lista.append(correcta)
    return lista

# Devuelve "opciones" que son las opciones de la respuesta enumeradas
def construir_opciones_enumeradas(json_raw):
    opciones = []
    opciones.append(respuesta_correcta(json_raw))
    for elemento in respuestas_incorrectas(json_raw):
        opciones.append(elemento)
    random.shuffle(opciones)
    return opciones

def determinar_acierto(json_raw, opciones, respuesta):
    if opciones[respuesta - 1] == respuesta_correcta(json_raw):
        print("Respuesta Correcta")
        return True
    else:
        print(f"Respuesta Incorrecta. La respuesta correcta es: {respuesta_correcta(json_raw)}")
        return False




def lanzar_pregunta():
    json_raw = get_json_raw(1)[0]
    opciones = construir_opciones_enumeradas(json_raw)
    print(sacar_pregunta(json_raw))
    print("\n")
    for indice, elemento in enumerate(opciones):
        print(f"{indice + 1}. {elemento}")
    print("\n")
    respuesta = int(input("Elige un número: "))
    determinar_acierto(json_raw, opciones, respuesta)
