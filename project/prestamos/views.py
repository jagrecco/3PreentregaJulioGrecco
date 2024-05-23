from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from . import forms, models

@login_required
def home(request):

    return render(request, 'prestamos/index.html')

@login_required
def listarprestamos(request):

    consulta=request.GET.get("consulta", None)

    if consulta:
        query = models.Prestamo.objects.filter(nombre__icontains=consulta)
    else:
        query=models.Prestamo.objects.all()

    context={'prestamos': query}

    return render(request, 'prestamos/listarprestamos.html', context)

@login_required
def crearprestamo(request):

    if request.method == "POST":

        form = forms.PrestamoCrearPrestamo(request.POST)

        if form.is_valid:
            form.save()
            return redirect("prestamos:home")
        
    else:  #si el request es GET entonces
        form = forms.PrestamoCrearPrestamo()

    return render(request, "prestamos/crearprestamo.html", context={"form": form})