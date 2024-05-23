from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . import models, forms

@login_required
def home(request):
        
    query=models.Usuario.objects.all()
    context={'usuarios': query}
    return render(request, 'usuarios/index.html', context)

@login_required
def listarusuarios(request):

    consulta = request.GET.get("consulta", None)

    if consulta:
        query = models.Usuario.objects.filter(nombre__icontains=consulta)
    else:
        query=models.Usuario.objects.all()
    
    context={'usuarios': query}
    return render(request, 'usuarios/listarusuarios.html', context)

@login_required
def crearusuario(request):

    if request.method == "POST":

        form = forms.CrearUsuario(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("usuarios:listarusuarios")
    else:
        form = forms.CrearUsuario()
    
    return render(request, "usuarios/crearusuario.html", context={"form": form})
        
