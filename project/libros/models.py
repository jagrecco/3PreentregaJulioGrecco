from django.db import models

class Autor(models.Model):
    nombre=models.CharField(max_length=200)
    descripcion=models.CharField(max_length=250,default='', null=True, blank=True)
    
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre=models.CharField(max_length=150)
    descripcion=models.CharField(max_length=250,default='', null=True, blank=True)

    def __str__(self) -> str:
        return self.nombre

class Libro(models.Model):
    nombre=models.CharField(max_length=150)
    autor=models.ForeignKey(Autor,on_delete=models.SET_NULL, null=True, blank=True, related_name = 'name')
    categoria=models.ForeignKey(Categoria,on_delete=models.SET_NULL, null=True, blank=True, related_name = 'name')
    stock=models.IntegerField(default=0)
    existencia=models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.nombre
