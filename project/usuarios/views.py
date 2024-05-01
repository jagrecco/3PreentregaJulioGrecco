from django.shortcuts import render
from . import models

def home(request):
    if (request.method=='GET'):
        print("fue un GET")
        
    query=models.Usuario.objects.all()
    context={'usuarios': query}
    return render(request, 'usuarios/index.html', context)