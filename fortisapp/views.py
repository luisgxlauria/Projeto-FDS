from django.shortcuts import render, redirect
from django.views import View
from .forms import UsuarioForm

class PaginaInicialView(View):
    def get(self, request):
        return render(request, 'html/PaginaInicial.html')

class loginView(View):
    def get(self, request):
        return render(request, "html/login.html")

class homeView(View):
    def get(self, request):
        return render(request, "html/home.html")

class hidratacaoView(View):
    def get(self, request):
        return render(request, "html/hidratacao.html")

def cadastroView(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')  # Certifique-se de que existe uma URL chamada 'sucesso'
    else:
        form = UsuarioForm()
    return render(request, 'html/cadastro.html', {'form': form})