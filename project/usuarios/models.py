from django.db import models

class Rol(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    mail = models.EmailField(max_length=250, unique=True, blank=False)

    def __str__(self):
        return f'{self.nombre}'

class Usuario(models.Model):
    name=models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, blank=True, related_name = 'name')
    pw=models.CharField(max_length=10, null=True, blank=True)
    rol=models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True, blank=True, related_name = 'rol')

    def __str__(self):
        return f'{self.name} | {self.rol}'
