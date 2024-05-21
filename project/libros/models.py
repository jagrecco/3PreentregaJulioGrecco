from django.db import models

class Autor(models.Model):
    nombre=models.CharField(max_length=200)
    nacionalidad=models.CharField(max_length=200, default='', null=True, blank=True)
    descripcion=models.TextField(max_length=250,default='', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Editorial(models.Model):
    nombre=models.CharField(max_length=200, default='', null=True, blank=True)
    pais=models.CharField(max_length=60, default='', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre=models.CharField(max_length=150)
    descripcion=models.TextField(max_length=250,default='', null=True, blank=True)

    def __str__(self) -> str:
        return self.nombre

class Libro(models.Model):
    titulo=models.CharField(max_length=150)
    autor=models.ForeignKey(Autor,on_delete=models.SET_NULL, null=True, blank=True, related_name = 'name')
    editorial=models.ForeignKey(Editorial,on_delete=models.SET_NULL, null=True, blank=True)
    genero=models.ForeignKey(Genero,on_delete=models.SET_NULL, null=True, blank=True)
    isbn=models.CharField(null=True, blank=True, max_length=50)
    anio=models.IntegerField(default=0, blank=True,null=True)
    descripcion=models.TextField(max_length=350,default='', null=True, blank=True)
    idioma=models.CharField(max_length=150, null=True, blank=True)
    paginas=models.IntegerField(default=0)
    stock=models.IntegerField(default=0)
    existencia=models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.titulo
