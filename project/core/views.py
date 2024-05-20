from django.contrib.auth.views import LoginView
from django.shortcuts import render

from .forms import CustonAuthenticationForm

def home(request):
    return render(request, "core/index.html")

class CustomLoginView(LoginView):
    authentication_form = CustonAuthenticationForm
    template_name = "core/login.html"