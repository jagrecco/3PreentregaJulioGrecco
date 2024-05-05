import sqlite3

# Conexión a la base de datos
conexion = sqlite3.connect("biblioteca.db")
cursor = conexion.cursor()

# Creación de las tablas (si no existen)
cursor.execute("""
CREATE TABLE IF NOT EXISTS libros (
    titulo TEXT NOT NULL,
    autor_id INTEGER NOT NULL,
    genero TEXT NOT NULL,
    FOREIGN KEY (autor_id) REFERENCES autores(id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS autores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_completo TEXT NOT NULL,
    resena TEXT
);
""")

# Inserción de los autores
autores = [
    ("Gabriel García Márquez", "Novelista, cuentista, guionista y periodista colombiano, ganador del Premio Nobel de Literatura en 1982. Su obra más conocida es Cien años de soledad."),
    ("J.R.R. Tolkien", "Filólogo y escritor británico, conocido principalmente por ser el autor de las obras de fantasía heroica El Señor de los Anillos y El Silmarillion."),
    # ... (Añadir el resto de los autores)
]

for nombre_completo, resena in autores:
    cursor.execute("INSERT INTO autores (nombre_completo, resena) VALUES (?, ?)", (nombre_completo, resena))

# Obtención de los IDs de los autores
autor_ids = {}
for autor in autores:
    cursor.execute("SELECT id FROM autores WHERE nombre_completo = ?", (autor[0],))
    autor_ids[autor[0]] = cursor.fetchone()[0]

# Inserción de los libros
libros = [
    ("Cien años de soledad", autor_ids["Gabriel García Márquez"], "Realismo mágico"),
    ("El Señor de los Anillos", autor_ids["J.R.R. Tolkien"], "Fantasía"),
    # ... (Añadir el resto de los libros)
]

for titulo, autor_id, genero in libros:
    cursor.execute("INSERT INTO libros (titulo, autor_id, genero) VALUES (?, ?, ?)", (titulo, autor_id, genero))

# Guardar los cambios y cerrar la conexión
conexion.commit()
conexion.close()
