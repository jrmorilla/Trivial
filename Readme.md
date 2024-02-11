# COSAS QUE IMPLEMENTAR

## Modo Carrera:

El modo carrera consiste en acertar todas las preguntas que puedas antes de que 
se te acaben las vidas.

La idea es tener habilitadas las siguientes features:

- Histórico de partidas con los siguientes datos: Preguntas acertadas y tiempo transcurrido

## Modo Normal

- Estadísticas de las preguntas acertadas y falladas
- Implementar dado
- Implementar pregunta normal
- Implementar pregunta de quesito

## Modo quién quiere ser millonario

- Introducir comodines
- Introducir tiempo
- Introducir mecánica original

## Estadísticas

- Implementar todo el código de recopilación
- Implementar todo el código de visualización

## Base de datos

### La base de datos de las preguntas tendrá el siguiente esquema:
Pregunta - [Respuestas] - Respuesta correcta - Topic - Dificultad

### La base de datos de los usuarios tendrá el siguiente esquema:

User - {Toppic: Preg_Totales} - {Toppic: Preg_Acertadas}


### La base de datos de estadísticas tendrá el siguiente esquema:

Topic - Dificultad - Evaluación
