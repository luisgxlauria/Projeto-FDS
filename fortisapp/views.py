from django.shortcuts import render, redirect
from django.views import View
from .forms import UsuarioForm, HidratacaoForm, LoginForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.db.models import Sum
from .models import Hidratacao
from .models import Peso
from .forms import PesoForm
from .forms import MetaPesoForm
from .models import MetaPeso

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
    
class historicohidratacaoView(View):
    def get(self, request):
        return render(request, "html/historicohidratacao.html")
    
class veja_imcView(View):
    def get (self, request):
        return render(request, "html/veja_imc.html")
    
class acompanha_imcView(View):
    def get(self, request):
        return render(request, "html/acompanha_imc.html")
    
class LoginViewCustom(LoginView):
    template_name = 'html/login.html'  # Template que será usado
    form_class = LoginForm  # Formulário de login personalizado
    redirect_authenticated_user = True  # Redireciona se o usuário já estiver logado

class tecnicaspbemestarView(View):
    def get(self, request):
        return render(request, "html/tecnicaspbemestar.html")
    
class relaxamentomuscularView(View):
    def get(self, request):
        return render(request, "html/relaxamentomuscular.html")

    def get_success_url(self):
        return reverse_lazy('home')  # Redireciona para a home após login
    
class respiracaoguiadaView(View):
    def get(self, request):
        return render (request, 'html/respiracaoguiada.html')
    
class alongamentoView(View):
    def get(self, request):
        return render(request, 'html/alongamento.html')

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

@login_required
def hidratacao(request):
    if request.method == 'POST':
        form = HidratacaoForm(request.POST)
        if form.is_valid():
            hidratacao = form.save(commit=False)
            hidratacao.usuario = request.user
            hidratacao.save()
            return redirect('hidratacao')
    else:
        form = HidratacaoForm()  # Aqui o formulário é instanciado e passado para o template

    hoje = now().date()
    total_diario = Hidratacao.objects.filter(
        usuario=request.user, data_hora__date=hoje
    ).aggregate(total=Sum('quantidade_agua'))['total'] or 0

    return render(request, 'html/hidratacao.html', {
        'form': form,  # Passa o formulário para o template
        'total_diario': total_diario
    })

def historicoHidratacao(request):
    # Busca todos os registros de hidratação do usuário logado, ordenados por data/hora
    historico = Hidratacao.objects.filter(usuario=request.user).order_by('-data_hora')

    # Passa o histórico para o template
    return render(request, 'html/historico_hidratacao.html', {
        'historico': historico
    })

def calcular_imc(request):
    imc = None
    if request.method == 'POST':
        peso = float(request.POST.get("peso"))
        altura = float(request.POST.get("altura"))
        imc = peso / (altura ** 2)  
    
    return render(request, "html/meupeso.html", {"imc": imc})

@login_required
def meupeso(request):
    if request.method == 'POST':
        form = PesoForm(request.POST)
        if form.is_valid():
            peso = form.save(commit=False)
            peso.usuario = request.user
            peso.save()
            return redirect('veja_imc')
    else:
        form = PesoForm()

    return render(request, 'html/meupeso.html', {'form': form})

@login_required
def veja_imc(request):
    # Busca o último registro de peso do usuário logado
    ultimo_registro = Peso.objects.filter(usuario=request.user).order_by('-data_registro').first()

    if ultimo_registro:
        imc = ultimo_registro.imc
        classificacao = classificar_imc(imc)
    else:
        imc = None
        classificacao = None

    # Lógica para salvar a meta
    meta_form = MetaPesoForm(request.POST or None)  # Alteração para não criar outro formulário em GET
    if request.method == 'POST' and meta_form.is_valid():
        meta = meta_form.save(commit=False)
        meta.usuario = request.user
        meta.save()
        return redirect('veja_imc')

    # Busca as metas existentes do usuário
    metas = MetaPeso.objects.filter(usuario=request.user).order_by('-data_criacao')

    # Busca todos os registros de IMC anteriores do usuário
    registros_imc = Peso.objects.filter(usuario=request.user).order_by('-data_registro')

    return render(request, 'html/veja_imc.html', {
        'imc': imc,
        'classificacao': classificacao,
        'form': meta_form,
        'metas': metas,
        'registros_imc': registros_imc  # Passa os registros de IMC anteriores para o template
    })

# Função que classifica o IMC
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"
