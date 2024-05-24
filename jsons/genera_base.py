import sqlite3
import json

# Leer los JSON de libros, autores y editoriales
with open('libros.json', 'r', encoding='utf-8') as file:
    libros_data = json.load(file)

with open('autores.json', 'r', encoding='utf-8') as file:
    autores_data = json.load(file)

with open('editoriales.json', 'r', encoding='utf-8') as file:
    editoriales_data = json.load(file)

with open('generos.json', 'r', encoding='utf-8') as file:
    generos_data = json.load(file)

# Crear una conexión a la base de datos SQLite
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()


for autor in autores_data:
    c.execute("INSERT INTO libros_autor (id, nombre, nacionalidad, descripcion) VALUES (?, ?, ?, ?)",
                   (autor["id"], autor["nombre"], autor["nacionalidad"], autor["descripcion"]))

for editorial in editoriales_data:
    c.execute("INSERT INTO libros_editorial (id, nombre, pais) VALUES (?, ?, ?)",
                   (editorial["id"], editorial["nombre"], editorial["pais"]))

for genero in generos_data:
    c.execute("INSERT INTO libros_genero (id, nombre, descripcion) VALUES (?, ?, ?)",
                   (genero["id"], genero["nombre"], genero["descripcion"]))

for libro in libros_data:
    c.execute("INSERT INTO libros_libro (id, titulo, autor, editorial, genero, año, paginas, idioma, isbn, descripcion) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (libro["id"], libro["titulo"], libro["autor"], libro["editorial"], libro["genero"], libro["año"], libro["paginas"], libro["idioma"], libro["isbn"], libro["descripcion"]))

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()


# Crear las tablas de autores y editoriales si no existen
""" c.execute('''CREATE TABLE IF NOT EXISTS autores (
                id INTEGER PRIMARY KEY,
                nombre TEXT,
                nacionalidad TEXT
            )''') """

""" c.execute('''CREATE TABLE IF NOT EXISTS editoriales (
                id INTEGER PRIMARY KEY,
                nombre TEXT
            )''') """

# Insertar los datos de autores en la tabla
""" for autor in autores_data:
    c.execute('''INSERT INTO libros_autor (id, nombre, nacionalidad,descripcion)
                VALUES (?, ?, ?)''',
              (autor['id'], autor['nombre'], autor['nacionalidad']),autor['descripcion'])
 """
# Insertar los datos de editoriales en la tabla
""" for editorial in editoriales_data:
    c.execute('''INSERT INTO libros_editorial (id, nombre, pais)
                VALUES (?, ?)''',
              (editorial['id'], editorial['nombre'], editorial['pais'])) """

# Insertar los datos de generos en la tabla
""" for genero in generos_data:
    c.execute('''INSERT INTO libros_genero (id, nombre, descripcion)
                VALUES (?, ?)''',
              (genero['id'], genero['nombre'], genero['descripcion'])) """

# Crear la tabla de libros si no existe
""" c.execute('''CREATE TABLE IF NOT EXISTS libros (
                id INTEGER PRIMARY KEY,
                titulo TEXT,
                autor_id INTEGER,
                editorial_id INTEGER,
                genero TEXT,
                anio_publicacion INTEGER,
                reseña TEXT,
                isbn TEXT,
                FOREIGN KEY (autor_id) REFERENCES autores (id),
                FOREIGN KEY (editorial_id) REFERENCES editoriales (id)
            )''')
 """
# Insertar los datos de libros en la tabla
""" for libro in libros_data:
    c.execute('''INSERT INTO libros_libro (id, titulo, autor, editorial, genero, isbn, anio, descripcion)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
              (libro['id'], libro['titulo'], libro['autor_id'], libro['editorial_id'], libro['genero'],
               libro['anio_publicacion'], libro['reseña'], libro['isbn']))
 """
# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Datos de libros, autores y editoriales insertados en la base de datos SQLite.")

