import pandas as pd
import sqlite3

conn = sqlite3.connect('base_datos_preguntas.db')

sql_query = "SELECT * FROM PREGUNTAS"

#sql_query_2 = "DELETE FROM PREGUNTAS WHERE PREGUNTA = '¿Qué significa H20?' "

sql_query_3 = "SELECT * FROM PREGUNTAS"

#resultado = conn.execute(sql_query_3)



#conn.execute(sql_query_2)

#conn.commit()

# Configurar pandas para mostrar todas las filas y columnas
pd.set_option('display.max_rows', None)  # Mostrar todas las filas
pd.set_option('display.max_columns', None)  # Mostrar todas las columnas



df = pd.read_sql_query(sql_query_3, conn)

print(df)