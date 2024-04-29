from django.shortcuts import render

from . import models

def home(request):
    query=models.Libro.objects.all()
    context={'libros': query}
    return render(request, 'libros/index.html', context)