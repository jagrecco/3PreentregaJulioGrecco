from django import forms

from . import models

class LibrosCrearAutor(forms.ModelForm):
    class Meta:
        model = models.Autor
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "nacionalidad": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }

class LibrosCrearEditorial(forms.ModelForm):
    class Meta:
        model=models.Editorial
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "pais": forms.TextInput(attrs={"class": "form-control"}),
        }

class LibrosCrearGenero(forms.ModelForm):
    class Meta:
        model=models.Genero
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control"}),
        }

class LibrosCrearLibro(forms.ModelForm):
    class Meta:
        model = models.Libro
        fields = '__all__'
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "autor" : forms.Select(attrs={"class": "form-control"}),
            "editorial" : forms.Select(attrs={"class": "form-control"}),
            "genero" : forms.Select(attrs={"class": "form-control"}),
            "isbn": forms.TextInput(attrs={"class": "form-control"}),
            "anio" : forms.NumberInput(attrs={'min': 0}),
            "descripcion": forms.Textarea(attrs={"class": "form-control"}),
            "stock" : forms.NumberInput(attrs={'min': 0}),
            "existencia" : forms.NumberInput(attrs={'min': 0}),
        }