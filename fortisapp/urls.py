from django.urls import path
from .views import PaginaInicialView, cadastroView, LoginViewCustom, homeView, hidratacao, meupesoView, estresseView, historicohidratacaoView, custom_logout_view, veja_imcView, acompanha_imcView, calcular_imc
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', PaginaInicialView.as_view(), name="PaginaInicial"), 
    path('cadastro/', cadastroView, name='cadastro'),  
    path('login/', LoginViewCustom.as_view(), name='login'), 
    path('logout/', custom_logout_view, name='logout'),  # Logout personalizado
    path('home/', homeView.as_view(), name='home'),  # Página inicial após o login
    path('hidratacao/', hidratacao, name='hidratacao'),
    path('sucesso/', LoginViewCustom.as_view(), name='sucesso'),  # Após o cadastro, redireciona para o login (ou ajuste conforme sua necessidade)
    path('meupeso/', meupesoView.as_view(), name="meupeso"),
    path('estresse/', estresseView.as_view(), name="estresse"),
    path('historicohidratacao/', historicohidratacaoView.as_view(), name='historicohidratacao'),  # Página de histórico de hidratação
    path('veja_imc/', veja_imcView.as_view(), name= "veja_imc"),
    path('acompanha_imc/', acompanha_imcView.as_view(), name= "acompanha_imc"),
    path('meupeso/', calcular_imc, name= "calcular_imc"),
]