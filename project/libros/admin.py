from django.contrib import admin

from . import models

admin.site.register(models.Autor)
admin.site.register(models.Genero)
admin.site.register(models.Libro)