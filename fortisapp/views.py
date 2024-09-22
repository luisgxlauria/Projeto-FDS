from django.shortcuts import render, redirect
from django.views import View
from .forms import CadastroForm
from django.contrib.auth import authenticate, login as lg
from django.contrib.auth.models import User

from fortisapp.models import fortis

class PaginaInicialView(View):
    def get(self, request):
        return render(request, 'html/PaginaInicial.html')
     
class loginView(View):
    def get(self, request):
        return render(request, "html/login.html")

class homeView(View):
    def get (self, request):
        return render (request, "html/home.html")
    
class hidratacaoView(View):
    def get(self, request):
        return render (request, "html/hidratacao.html")
    
class cadastroView(View):
    def get(self, request):
        form = CadastroForm()
        return render(request, 'html/cadastro.html', {'form': form})

    def post(self, request):
        form = CadastroForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            cpf = form.cleaned_data['cpf']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            return redirect('login')
        return render(request, 'cadastro.html', {'form': form})