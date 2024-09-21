from django.shortcuts import render, redirect
from django.views import View

from django.contrib.auth import authenticate, login as lg
from django.contrib.auth.models import User

from fortisapp.models import fortis

class PaginaInicialView(View):
    def get(self, request):
        return render(request, 'html/PaginaInicial.html')
    
class cadastroView(View):
    def get(self, request):
        return render(request, 'html/cadastro.html')
    
class loginView(View):
    def get(self, request):
        return render(request, "html/login.html")

class homeView(View):
    def get (self, request):
        return render (request, "html/home.html")
    
class hidratacaoView(View):
    def get(self, request):
        return render (request, "html/hidratacao.html")