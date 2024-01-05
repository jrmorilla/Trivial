import funciones_funcionalidad
import funciones_preguntas

def instrucciones():
    return "Escribir instrucciones\n"
def jugar_carrera():
    print(instrucciones())
    num_preguntas = funciones_funcionalidad.seleccion_num_preguntas()
    categoria = funciones_funcionalidad.seleccion_categoria()
    dificultad = funciones_funcionalidad.seleccion_dificultad()
    funciones_funcionalidad.jugar_modo_carrera(num_preguntas, categoria, dificultad)