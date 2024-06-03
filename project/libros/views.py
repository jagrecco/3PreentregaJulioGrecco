from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from . import forms, models

#autor= models.Autor.objects.all().values('url')
#genero= models.Genero.objects.all()

def home(request):
    
    return render(request, 'libros/index.html')

#Vistas para libros
@login_required
def listarlibros(request):

    consulta = request.GET.get("consulta", None)

    if consulta:
        query = models.Libro.objects.filter(titulo__icontains=consulta)
    else:
        query=models.Libro.objects.all().select_related('autor')[:10]
    
    context={'libros': query} #, 'autor': autor
    return render(request, 'libros/listarlibros.html', context)

@login_required
def crearlibro(request):
    if request.method == "POST":
        form = forms.LibrosCrearLibro(request.POST)
        if form.is_valid:
            form.save()
            return redirect("libros:listarlibros")
    else:
        form = forms.LibrosCrearLibro()
    return render(request, "libros/crearlibro.html", context={"form": form})

@login_required
def editarlibro(request, pk : int):
    query=models.Libro.objects.get(id=pk)
    if request.method == 'POST':
        form = forms.LibrosCrearLibro(request.POST, instance=query)
        if form.is_valid:
            form.save()
            return redirect('libros:listarlibros')
    else:
        form = forms.LibrosCrearLibro(instance=query)
    return render(request, "libros/crearlibro.html", context={"form": form})

@login_required
def eliminarlibro(request, pk : int):
    query=models.Libro.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('libros:listarlibros')
    
    return render(request, "libros/eliminarlibro.html", context={"libro": query})

#Vistas para Autores
@login_required
def listarautores(request):

    consulta=request.GET.get("consulta", None)

    if consulta:
        query = models.Autor.objects.filter(nombre__icontains=consulta)
    else:
        query=models.Autor.objects.all()

    context={'autores': query}
    return render(request, 'libros/listarautores.html', context)

@login_required
def crearautor(request):
    if request.method == "POST":
        form = forms.LibrosCrearAutor(request.POST)
        if form.is_valid:
            form.save()
            return redirect("libros:listarautores")
    else:  #si el reques es GET entonces
        form = forms.LibrosCrearAutor()
    return render(request, "libros/crearautor.html", context={"form": form})

@login_required
def editarautor(request, pk: int):
    query=models.Autor.objects.get(id=pk)
    if request.method == 'POST':
        form = forms.LibrosCrearAutor(request.POST, instance=query)
        if form.is_valid:
            form.save()
            return redirect('libros:listarautores')
    else:  #si el reques es GET entonces
        form = forms.LibrosCrearAutor(instance=query)
    return render(request, "libros/crearautor.html", context={"form": form})

@login_required
def eliminarautor(request, pk: int):
    query=models.Autor.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('libros:listarautores')
    
    return render(request, "libros/eliminarautor.html", context={"autor": query})


#Vistas para Generos
@login_required
def listargeneros(request):

    consulta=request.GET.get("consulta", None)

    if consulta:
        query = models.Genero.objects.filter(nombre__icontains=consulta)
    else:
        query=models.Genero.objects.all()

    context={'generos': query}
    return render(request, 'libros/listargeneros.html', context)

@login_required
def creargenero(request):
    
    if request.method == "POST":
        form = forms.LibrosCrearGenero(request.POST)
        if form.is_valid:
            form.save()
            return redirect("libros:listargeneros")
    else:
        form = forms.LibrosCrearGenero()
    return render(request, "libros/creargenero.html", context={"form": form})

@login_required
def eliminagenero(request, pk:int):
    query=models.Genero.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('libros:listargeneros')
    
    return render(request, "libros/eliminagenero.html", context={"categoria": query})

@login_required
def editargenero(request, pk: int):
    query=models.Genero.objects.get(id=pk)
    if request.method == 'POST':
        form = forms.LibrosCrearGenero(request.POST, instance=query)
        if form.is_valid:
            form.save()
            return redirect('libros:listargeneros')
    else:
        form = forms.LibrosCrearAutor(instance=query)
    return render(request, "libros/creargenero.html", context={"form": form})