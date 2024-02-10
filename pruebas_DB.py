import sqlite3

conn = sqlite3.connect('base_datos_preguntas.db')

# Crear una tabla
import json

# Crear la tabla
conn.execute('''CREATE TABLE IF NOT EXISTS PREGUNTAS (
                PREGUNTA TEXT NOT NULL,
                RESPUESTAS TEXT,
                RESPUESTA_CORRECTA TEXT,
                TOPIC TEXT,
                DIFFICULTY TEXT
                )''')

# Insertar datos
pregunta = "De qué color es una manzana?"
respuestas = ['Rojo', 'Lila']
respuestas_serializadas = json.dumps(respuestas)

conn.execute("INSERT INTO PREGUNTAS (PREGUNTA, RESPUESTAS, RESPUESTA_CORRECTA, TOPIC, DIFFICULTY) VALUES (?, ?, ?, ?, ?)", (pregunta, respuestas_serializadas, 'Rojo', 'Cultura General', 'Fácil'))

conn.commit()

cursor = conn.cursor()

cursor.execute("SELECT * FROM PREGUNTAS")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()


