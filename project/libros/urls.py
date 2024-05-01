from django.urls import path

from . import views

app_name = 'libros'

urlpatterns = [
    path('', views.home, name='home'),
    #Rutas para libros
    path('libros',views.listarlibros,name='listarlibros'),

    #Rutas para autores
    path('autores',views.listarautores,name='listarautores'),
    path('crearautor',views.crearautor,name='crearautor'),
    path('editarautor/<int:pk>',views.editarautor,name='editarautor'),
    path('eliminarautor/<int:pk>',views.eliminarautor,name='eliminarautor'),
  
    #Rutas para categorias
    path('categorias',views.listarcategorias,name='listarcategorias'),

]
