import inicializacion
import funciones_preguntas
import funciones_funcionalidad

if inicializacion.iniciar_juego() == 1:
    num_preguntas = inicializacion.get_num_preguntas()
    funciones_funcionalidad.jugar_modo_normal(num_preguntas)
elif inicializacion.iniciar_juego() == 3:
    funciones_funcionalidad.jugar_modo_carrera(10, 3, 'easy')
else:
    print("Esta opción aun no está programada")