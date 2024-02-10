import sqlite3
import json

def crear_DB_PREGUNTAS():
    conn = conectar_DB('base_datos_preguntas.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS PREGUNTAS (
                    PREGUNTA TEXT NOT NULL,
                    RESPUESTAS TEXT,
                    RESPUESTA_CORRECTA TEXT,
                    TOPIC TEXT,
                    DIFFICULTY TEXT
                    )''')
def conectar_DB(DB_FILE):
    return sqlite3.connect(DB_FILE)

def desconectar_DB(DB_FILE):
    return conectar_DB(DB_FILE).close()

def commit_DB(DB_FILE):
    return conectar_DB(DB_FILE).commit()

def comprobar_existencia_pregunta_DB(PREGUNTA):
    # Conectamos con la base de datos
    conn = conectar_DB('base_datos_preguntas.db')

    # Crear un cursor
    cursor = conn.cursor()

    # Consultar la base de datos para ver si la pregunta está presente
    cursor.execute("SELECT PREGUNTA FROM PREGUNTAS WHERE PREGUNTA = ?", (PREGUNTA,))
    resultado = cursor.fetchone()

    if resultado:
        return True
    else:
        return False
def añadir_datos_pregunta(PREGUNTA: str, RESPUESTAS: list, RESPUESTA_CORRECTA: str, TOPIC: str, DIFICULTAD: str):
    try:
        conn = conectar_DB('base_datos_preguntas.db')
        conn.execute('''CREATE TABLE IF NOT EXISTS PREGUNTAS (
                        PREGUNTA TEXT NOT NULL,
                        RESPUESTAS TEXT,
                        RESPUESTA_CORRECTA TEXT,
                        TOPIC TEXT,
                        DIFFICULTY TEXT
                        )''')
        respuestas_serializadas = json.dumps(RESPUESTAS)
        conn.execute(
            "INSERT INTO PREGUNTAS (PREGUNTA, RESPUESTAS, RESPUESTA_CORRECTA, TOPIC, DIFFICULTY) VALUES (?, ?, ?, ?, ?)",
            (PREGUNTA, respuestas_serializadas, RESPUESTA_CORRECTA, TOPIC, DIFICULTAD))
        conn.commit()
        conn.close()
        return True
    except ValueError as e:
        raise e

