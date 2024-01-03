import requests


def obtener_preguntas_trivial(cantidad=10):
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


def estructurar_preguntas(preguntas):
    estructura_formateada = []

    for idx, pregunta in enumerate(preguntas, start=1):
        pregunta_formateada = f"Pregunta {idx}: {pregunta['question']}\n"

        # Formatear las opciones (incorrectas y correcta)
        opciones = pregunta['incorrect_answers'] + [pregunta['correct_answer']]
        opciones_formateadas = [f"Opción {i + 1}: {opcion}" for i, opcion in enumerate(opciones)]

        # Agregar las opciones formateadas a la pregunta formateada
        pregunta_formateada += '\n'.join(opciones_formateadas)

        estructura_formateada.append(pregunta_formateada)

    return estructura_formateada

for i in estructurar_preguntas(obtener_preguntas_trivial(10)):
    print(i)