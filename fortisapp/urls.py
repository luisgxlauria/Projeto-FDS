from django.urls import path
from .views import LoginViewCustom
from .views import PaginaInicialView, cadastroView, LoginViewCustom, homeView, hidratacaoView, meupesoView, estresseView
from django.contrib.auth.views import LogoutView
from .views import custom_logout_view

urlpatterns = [
    path('', PaginaInicialView.as_view(), name="PaginaInicial"),  # Página inicial
    path('cadastro/', cadastroView, name='cadastro'),  # Página de cadastro
    path('login/', LoginViewCustom.as_view(), name='login'),  # Página de login
    path('logout/', custom_logout_view, name='logout'),  # Logout personalizado
    path('home/', homeView.as_view(), name='home'),  # Página inicial após o login
    path('hidratacao/', hidratacaoView.as_view(), name="hidratacao"),  # Página de hidratação
    path('sucesso/', LoginViewCustom.as_view(), name='sucesso'),  # Após o cadastro, redireciona para o login (ou ajuste conforme sua necessidade)
    path('meupeso/', meupesoView.as_view(), name="meupeso"),
    path('estresse/', estresseView.as_view(), name="estresse")
]