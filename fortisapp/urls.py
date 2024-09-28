from django.urls import path
from .views import PaginaInicialView, cadastroView, LoginViewCustom, homeView, hidratacaoView, meupesoView, estresseView, histhidratacaoView, custom_logout_view, historicoHidratacaoView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', PaginaInicialView.as_view(), name="PaginaInicial"), 
    path('cadastro/', cadastroView, name='cadastro'),  
    path('login/', LoginViewCustom.as_view(), name='login'), 
    path('logout/', custom_logout_view, name='logout'),  # Logout personalizado
    path('home/', homeView.as_view(), name='home'),  # Página inicial após o login
    path('hidratacao/', hidratacaoView, name='hidratacao'),
    path('sucesso/', LoginViewCustom.as_view(), name='sucesso'),  # Após o cadastro, redireciona para o login (ou ajuste conforme sua necessidade)
    path('meupeso/', meupesoView.as_view(), name="meupeso"),
    path('estresse/', estresseView.as_view(), name="estresse"),
    path('historico_hidratacao/', historicoHidratacaoView, name='histhidratacao'),  # Página de histórico de hidratação
]