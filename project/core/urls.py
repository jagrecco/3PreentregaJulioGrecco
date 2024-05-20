from django.urls import path
from . import views

app_name= 'core'

urlpatterns = [
    path('',views.home, name='home'),
    path('login/', views.CustomLoginView.as_view(), name='login')
]