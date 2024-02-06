import sqlite3

conn = sqlite3.connect('mi_base_de_datos.db')

# Crear una tabla
conn.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                edad INTEGER
                )''')

# Insertar datos
conn.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ('Juan', 30))
conn.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ('María', 25))

conn.commit()

cursor = conn.cursor()

cursor.execute("SELECT * FROM usuarios")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()


