from django.urls import path

from . import views

app_name = 'libros'

urlpatterns = [
    path('', views.home, name='home'),
    #Rutas para libros
    path('libros',views.listarlibros,name='listarlibros'),
    path('crearlibro',views.crearlibro,name='crearlibro'),
    path('editarlibro/<int:pk>',views.editarlibro,name='editarlibro'),
    path('eliminarlibro/<int:pk>',views.eliminarlibro,name='eliminarlibro'),

    #Rutas para autores
    path('autores',views.listarautores,name='listarautores'),
    path('crearautor',views.crearautor,name='crearautor'),
    path('editarautor/<int:pk>',views.editarautor,name='editarautor'),
    path('eliminarautor/<int:pk>',views.eliminarautor,name='eliminarautor'),
  
    #Rutas para géneros
    path('generos',views.listargeneros,name='listargeneros'),
    path('creargenero',views.creargenero,name='creargenero'),
    path('eliminagenero/<int:pk>',views.eliminagenero,name='eliminagenero'),
    path('editargenero/<int:pk>',views.editargenero,name='editargenero'),
]
