from django.shortcuts import render, redirect

from . import forms, models

def home(request):
    #query=models.Libro.objects.all()
    #context={'libros': query}
    return render(request, 'libros/index.html')

#Vistas para libros
def listarlibros(request):

    consulta = request.GET.get("consulta", None)

    if consulta:
        query = models.Libro.objects.filter(titulo__icontains=consulta)
    else:
        query=models.Libro.objects.all()
    
    context={'libros': query}
    return render(request, 'libros/listarlibros.html', context)

def crearlibro(request):
    if request.method == "POST":
        form = forms.LibrosCrearLibro(request.POST)
        if form.is_valid:
            form.save()
            return redirect("libros:home")
    else:
        form = forms.LibrosCrearLibro()
    return render(request, "libros/crearlibro.html", context={"form": form})

def editarlibro(request, pk : int):
    query=models.Libro.objects.get(id=pk)
    if request.method == 'POST':
        form = forms.LibrosCrearLibro(request.POST, instance=query)
        if form.is_valid:
            form.save()
            return redirect('libros:home')
    else:
        form = forms.LibrosCrearLibro(instance=query)
    return render(request, "libros/crearlibro.html", context={"form": form})

def eliminarlibro(request, pk : int):
    query=models.Libro.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('libros:home')
    
    return render(request, "libros/eliminarlibro.html", context={"libro": query})

#Vistas para Autores
def listarautores(request):

    consulta=request.GET.get("consulta", None)

    if consulta:
        query = models.Autor.objects.filter(nombre__icontains=consulta)
    else:
        query=models.Autor.objects.all()

    context={'autores': query}
    return render(request, 'libros/listarautores.html', context)

def crearautor(request):
    if request.method == "POST":
        form = forms.LibrosCrearAutor(request.POST)
        if form.is_valid:
            form.save()
            return redirect("libros:home")
    else:  #si el reques es GET entonces
        form = forms.LibrosCrearAutor()
    return render(request, "libros/crearautor.html", context={"form": form})

def editarautor(request, pk: int):
    query=models.Autor.objects.get(id=pk)
    if request.method == 'POST':
        form = forms.LibrosCrearAutor(request.POST, instance=query)
        if form.is_valid:
            form.save()
            return redirect('libros:home')
    else:  #si el reques es GET entonces
        form = forms.LibrosCrearAutor(instance=query)
    return render(request, "libros/crearautor.html", context={"form": form})

def eliminarautor(request, pk: int):
    query=models.Autor.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('libros:home')
    
    return render(request, "libros/eliminarautor.html", context={"autor": query})


#Vistas para Generos
def listargeneros(request):

    consulta=request.GET.get("consulta", None)

    if consulta:
        query = models.Genero.objects.filter(nombre__icontains=consulta)
    else:
        query=models.Genero.objects.all()

    context={'generos': query}
    return render(request, 'libros/listargeneros.html', context)

def creargenero(request):
    if request.method == "POST":
        form = forms.LibrosCrearGenero(request.POST)
        if form.is_valid:
            form.save()
            return redirect("libros:home")
    else:
        form = forms.LibrosCrearGenero()
    return render(request, "libros/creargenero.html", context={"form": form})

def eliminagenero(request, pk:int):
    query=models.Genero.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('libros:home')
    
    return render(request, "libros/eliminagenero.html", context={"categoria": query})

def editargenero(request, pk: int):
    query=models.Genero.objects.get(id=pk)
    if request.method == 'POST':
        form = forms.LibrosCrearGenero(request.POST, instance=query)
        if form.is_valid:
            form.save()
            return redirect('libros:home')
    else:
        form = forms.LibrosCrearAutor(instance=query)
    return render(request, "libros/editargenero.html", context={"form": form})