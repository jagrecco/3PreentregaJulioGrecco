from django.db import models
from django.utils import timezone

class Autor(models.Model):
    nombre=models.CharField(max_length=200)
    nacionalidad=models.CharField(max_length=200, default='', null=True, blank=True)
    url=models.CharField(max_length=250,default='', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre=models.CharField(max_length=150)
    url=models.CharField(max_length=250, default='', null=True, blank=True)

    def __str__(self) -> str:
        return self.nombre

class Libro(models.Model):
    titulo=models.CharField(max_length=150)
    autor=models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True, blank=True)
    editorial=models.CharField(null=True, blank=True, max_length=150)
    genero=models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True, blank=True)
    isbn=models.CharField(null=True, blank=True, max_length=50)
    anio=models.IntegerField(default=0, blank=True,null=True)
    idioma=models.CharField(max_length=150, null=True, blank=True)
    modificacion=models.DateTimeField(null=True, blank=True, default=timezone.now, editable=False, verbose_name="fecha de modificacion")
    paginas=models.IntegerField(default=0)
    nota=models.TextField(null=True, blank=True)
    stock=models.IntegerField(default=0)
    existencia=models.IntegerField(default=0)
    
    class Meta:
        ordering = ("-modificacion",)

    def __str__(self) -> str:
        return self.titulo
