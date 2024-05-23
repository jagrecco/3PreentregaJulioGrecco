from django import forms

from . import models

""" class CrearPersona(forms.ModelForm):

    class Meta:
        model = models.Persona
        fields = "__all__"
        widgets={
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "mail": forms.EmailInput(attrs={"class": "form-control"}),
        }
 """
class CrearRol(forms.ModelForm):

    class Meta:
        model = models.Rol
        fields = "__all__"
        widgets={
            "nombre" : forms.TextInput(attrs={"class": "form-control"}),
            "descripcion" : forms.Textarea(attrs={"class": "form-control"})
        }

class CrearUsuario(forms.ModelForm):

    class Meta:
        model = models.Usuario
        fields = "__all__"
        widgets = {
            "usuario" : forms.Select(attrs={"class" : "form-control"}),
            "rol" : forms.Select(attrs={"class" : "form-control"}),
            "mail": forms.EmailInput(attrs={"class": "form-control"}),
            "avatar": forms.FileInput(attrs={"class": "form-control"})
        }