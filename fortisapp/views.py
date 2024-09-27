from django.shortcuts import render, redirect
from django.views import View
from .forms import UsuarioForm
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import redirect

class PaginaInicialView(View):
    def get(self, request):
        return render(request, 'html/PaginaInicial.html')

class homeView(View):
    def get(self, request):
        return render(request, "html/home.html")

class hidratacaoView(View):
    def get(self, request):
        return render(request, "html/hidratacao.html")
    
class meupesoView(View):
    def get(self, request):
        return render(request, "html/meupeso.html")
    
class estresseView(View):
    def get(self, request):
        return render(request, "html/tecnicaspbemestar.html")
    
class LoginViewCustom(LoginView):
    template_name = 'html/login.html'  # Template que será usado
    form_class = LoginForm  # Formulário de login personalizado
    redirect_authenticated_user = True  # Redireciona se o usuário já estiver logado

    def get_success_url(self):
        return reverse_lazy('home')  # Redireciona para a home após login

def cadastroView(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')  # Certifique-se de que existe uma URL chamada 'sucesso'
    else:
        form = UsuarioForm()
    return render(request, 'html/cadastro.html', {'form': form})

def custom_logout_view(request):
    logout(request)
    return redirect('login')  # Redireciona para a página de login após o logout