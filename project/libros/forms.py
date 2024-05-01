from django import forms

from . import models

class LibrosCrearAutor(forms.ModelForm):
    class Meta:
        model = models.Autor
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }