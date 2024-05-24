import sqlite3
import json
import random

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

#for autor in autores_data:
#    c.execute("INSERT INTO libros_autor (id, nombre, nacionalidad, descripcion) VALUES (?, ?, ?, ?)",
#                   (autor["id"], autor["nombre"], autor["nacionalidad"], autor["descripcion"]))

#for editorial in editoriales_data:
#    c.execute("INSERT INTO libros_editorial (id, nombre, pais) VALUES (?, ?, ?)",
#                   (editorial["id"], editorial["nombre"], editorial["pais"]))

#for genero in generos_data:
#    c.execute("INSERT INTO libros_genero (id, nombre, descripcion) VALUES (?, ?, ?)",
#                   (genero["id"], genero["nombre"], genero["descripcion"]))


for libro in libros_data:
    candidad=random.randint(1, 5)
    existe=random.randint(0,5)
    c.execute("INSERT INTO libros_libro (id, stock, existencia, autor_id, titulo, anio, descripcion, isbn, editorial_id, genero_id, paginas, idioma) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (libro["id"], candidad, existe, libro["autor"], libro["titulo"], libro["año"], libro["descripcion"], libro["isbn"], libro["editorial"], libro["genero"],  libro["paginas"], libro["idioma"]))


""" for editorial in editoriales_data:
    c.execute("INSERT INTO libros_editorial (id, nombre, pais) VALUES (?, ?, ?)",
                   (editorial["id"], editorial["nombre"], editorial["pais"]))

for genero in generos_data:
    c.execute("INSERT INTO libros_genero (id, nombre, descripcion) VALUES (?, ?, ?)",
                   (genero["id"], genero["nombre"], genero["descripcion"]))

for libro in libros_data:
    c.execute("INSERT INTO libros_libro (id, titulo, autor, editorial, genero, año, paginas, idioma, isbn, descripcion) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (libro["id"], libro["titulo"], libro["autor"], libro["editorial"], libro["genero"], libro["año"], libro["paginas"], libro["idioma"], libro["isbn"], libro["descripcion"])) """

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()

# Guardar los cambios y cerrar la conexión
#conn.commit()
#conn.close()

print("Datos de libros, autores y editoriales insertados en la base de datos SQLite.")

