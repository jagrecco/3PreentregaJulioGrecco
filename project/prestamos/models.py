from django.db import models

from libros.models import Libro
from usuarios.models import Usuario

class Prestamo(models.Model):
    fechaAlta=models.DateField(auto_now=True)
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    libro=models.ForeignKey(Libro, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.libro} > Fecha préstamo: {self.fechaAlta}'