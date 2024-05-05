from django.urls import path

from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.home, name='home'),
    path('usuarios', views.listarusuarios, name='listarusuarios'),
    path('crearusuario', views.crearusuario, name='crearusuario'),
]