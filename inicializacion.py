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
    pass

def get_num_preguntas():
    print("Bienvenido al Trivial! Por favor, inserte el número de preguntas que quieres jugar: ")
    num_preguntas = int(input("Introduce un número: "))
    return num_preguntas

