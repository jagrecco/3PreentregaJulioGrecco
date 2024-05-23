from django.db import models
from django.contrib.auth.models import User

class Rol(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name="usuario")
    mail = models.EmailField(max_length=250, unique=True, blank=False, null=True)
    rol= models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True, blank=True, related_name = 'rol')
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f'{self.usuario.username} | {self.rol}'
