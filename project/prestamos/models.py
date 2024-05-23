from django.db import models

from libros.models import Libro
#from usuarios.models import Usuario
from django.contrib.auth.models import User

class Prestamo(models.Model):
    fechaAlta=models.DateField(auto_now=True)
    usuario=models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    libro=models.ForeignKey(Libro, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.libro.titulo} > Fecha préstamo: {self.fechaAlta}'