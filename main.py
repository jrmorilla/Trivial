import inicializacion
import funciones_preguntas
import funciones_funcionalidad

if inicializacion.iniciar_juego() == 1:
    num_preguntas = inicializacion.get_num_preguntas()
    funciones_funcionalidad.jugar(num_preguntas)
else:
    print("Esta opción aun no está programada")