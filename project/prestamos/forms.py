from django import forms

from . import models


class PrestamoCrearPrestamo(forms.ModelForm):

    class Meta:
        model = models.Prestamo
        fields = "__all__"
        widgets = {
            "fechaAlta": forms.DateField(),
            "usuario": forms.Select(attrs={"class": "form-control"}),
            "libro": forms.Select(attrs={"class": "form-control"}),
        }
