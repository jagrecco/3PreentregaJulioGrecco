from django.shortcuts import render
from . import models

def home(request):
    query=models.Usuario.objects.all()
    context={'usuarios': query}
    return render(request, 'usuarios/index.html', context)