from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

import random

from .forms import CustonAuthenticationForm, CustomUserCreationForm

citas = [
    {"cita": "La única forma de vencer la tentación es ceder ante ella.", "autor": "Oscar Wilde"},
    {"cita": "El único modo de hacer un gran trabajo es amar lo que haces.", "autor": "Steve Jobs"},
    {"cita": "La vida es lo que pasa mientras estás ocupado haciendo otros planes.", "autor": "Allen Saunders"},
    {"cita": "La imaginación es más importante que el conocimiento.", "autor": "Albert Einstein"},
    {"cita": "No hay caminos para la paz; la paz es el camino.", "autor": "Mahatma Gandhi"},
    {"cita": "La verdadera medida de un hombre no se ve en momentos de comodidad, sino en momentos de desafío y controversia.", "autor": "Martin Luther King Jr."},
    {"cita": "La mente que se abre a una nueva idea nunca volverá a su tamaño original.", "autor": "Albert Einstein"},
    {"cita": "No hay nada más poderoso en el mundo que una idea cuyo tiempo ha llegado.", "autor": "Víctor Hugo"},
    {"cita": "El arte es la mentira que nos permite conocer la verdad.", "autor": "Pablo Picasso"},
    {"cita": "La felicidad no se encuentra en vivir sin problemas, sino en superarlos.", "autor": "Ralph Waldo Emerson"},
    {"cita": "La educación es el arma más poderosa que puedes usar para cambiar el mundo.", "autor": "Nelson Mandela"},
    {"cita": "La libertad no vale la pena tener si no incluye la libertad de cometer errores.", "autor": "Mahatma Gandhi"},
    {"cita": "El hombre es libre en el momento en que desea serlo.", "autor": "Voltaire"},
    {"cita": "La paciencia es amarga, pero su fruto es dulce.", "autor": "Jean-Jacques Rousseau"},
    {"cita": "No se puede encontrar la paz evitando la vida.", "autor": "Virginia Woolf"},
    {"cita": "Lo que no me mata, me hace más fuerte.", "autor": "Friedrich Nietzsche"},
    {"cita": "El pesimista se queja del viento; el optimista espera que cambie; el realista ajusta las velas.", "autor": "William Arthur Ward"},
    {"cita": "La vida es lo que pasa mientras estamos ocupados haciendo planes.", "autor": "John Lennon"},
    {"cita": "La verdad es una tierra sin caminos.", "autor": "Jiddu Krishnamurti"},
    {"cita": "La religión es el suspiro de la criatura oprimida, el corazón de un mundo sin corazón y el alma de situaciones desalmadas.", "autor": "Karl Marx"},
    {"cita": "La muerte es el último y más grandioso de todos los misterios.", "autor": "E.M. Forster"},
    {"cita": "El que tiene un porqué para vivir puede soportar casi cualquier cómo.", "autor": "Friedrich Nietzsche"},
    {"cita": "La sabiduría es no tener opiniones.", "autor": "Friedrich Nietzsche"},
    {"cita": "La felicidad no es algo que se pospone para el futuro; es algo que se diseña para el presente.", "autor": "Jim Rohn"},
    {"cita": "La vida no es sino una continua sucesión de oportunidades para sobrevivir.", "autor": "Gabriel García Márquez"},
    {"cita": "Las palabras son como las hojas; cuando abundan, poco fruto hay entre ellas.", "autor": "Alexander Pope"},
    {"cita": "Las guerras seguirán mientras el color de la piel siga siendo más importante que el de los ojos.", "autor": "Bob Marley"},
    {"cita": "Soy el amo de mi destino; soy el capitán de mi alma.", "autor": "William Ernest Henley"},
    {"cita": "La lectura es a la mente lo que el ejercicio al cuerpo.", "autor": "Joseph Addison"},
    {"cita": "La mente que se abre a una nueva idea nunca volverá a su tamaño original.", "autor": "Albert Einstein"}
]

def home(request):
    #Renderiza un slogan diferente cada vez que se carga la página tomando como base la lista slogans
    numero_de_cita=random.randint(0, 29)
    return render(request, "core/index.html", {"cita": citas[numero_de_cita]["cita"],"autor": citas[numero_de_cita]["autor"]})

class CustomLoginView(LoginView):
    authentication_form = CustonAuthenticationForm
    template_name = "core/login.html"

def register(request:HttpRequest)-> HttpResponse:
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            form.save()
            return render(request,"core/index.html", {"mensaje": "Usuario creado"})
    else:
        form = CustomUserCreationForm()
    return render(request,"core/registro.html", {"form":form})