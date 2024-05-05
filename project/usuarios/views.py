from django.shortcuts import render, redirect
from . import models, forms

def home(request):
        
    query=models.Usuario.objects.all()
    context={'usuarios': query}
    return render(request, 'usuarios/index.html', context)

def listarusuarios(request):

    consulta = request.GET.get("consulta", None)

    if consulta:
        query = models.Usuario.objects.filter(nombre__icontains=consulta)
    else:
        query=models.Usuario.objects.all()
    
    context={'usuarios': query}
    return render(request, 'usuarios/listarusuarios.html', context)

def crearusuario(request):

    if request.method == "POST":
        form = forms.CrearPersona(request.POST)
        if form.is_valid:
            form.save()
            return redirect("usuarios:home")
    else:
        form = forms.CrearPersona()
    
    return render(request, "usuarios/crearusuario.html", context={"form": form})
        
