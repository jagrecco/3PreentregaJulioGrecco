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

class LibrosCrearCategoria(forms.ModelForm):
    class Meta:
        model = models.Categoria
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }

class LibrosCrearLibro(forms.ModelForm):
    class Meta:
        model = models.Libro
        fields = '__all__'
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "autor" : forms.Select(attrs={"class": "form-control"}),
            "categoria" : forms.Select(attrs={"class": "form-control"}),
            "stock" : forms.NumberInput(attrs={'min': 0}),
            "existencia" : forms.NumberInput(attrs={'min': 0}),
        }