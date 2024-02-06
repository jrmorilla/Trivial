import pandas as pd
import sqlite3

conn = sqlite3.connect('mi_base_de_datos.db')

sql_query = "SELECT * FROM usuarios"

df = pd.read_sql_query(sql_query, conn)

print(df)