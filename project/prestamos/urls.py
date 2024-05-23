from django.urls import path

from . import views

app_name = 'prestamos'

urlpatterns = [
    path('', views.home, name='home'),
    #Rutas para libros
    path('listarprestamos',views.listarprestamos, name='listarprestamos'),
    path('crearprestamo',views.crearprestamo, name='crearprestamo'),
    
]
