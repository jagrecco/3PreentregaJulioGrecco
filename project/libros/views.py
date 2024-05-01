from django.shortcuts import render, redirect

from . import forms, models

def home(request):
    #query=models.Libro.objects.all()
    #context={'libros': query}
    return render(request, 'libros/index.html')

#Vistas para libros
def listarlibros(request):
    query=models.Libro.objects.all()
    context={'libros': query}
    return render(request, 'libros/listarlibros.html', context)

#Vistas para Autores
def listarautores(request):
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





#Vistas para Categorias
def listarcategorias(request):
    query=models.Categoria.objects.all()
    context={'categorias': query}
    return render(request, 'libros/listarcategorias.html', context)
