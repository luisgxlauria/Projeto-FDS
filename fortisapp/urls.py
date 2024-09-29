from django.urls import path
from .views import PaginaInicialView, cadastroView, LoginViewCustom, homeView, hidratacao, meupeso, estresseView, historicohidratacaoView, custom_logout_view, veja_imcView, acompanha_imcView, veja_imc, tecnicaspbemestarView, relaxamentomuscularView, respiracaoguiadaView, alongamentoView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', PaginaInicialView.as_view(), name="PaginaInicial"), 
    path('cadastro/', cadastroView, name='cadastro'),  
    path('login/', LoginViewCustom.as_view(), name='login'), 
    path('logout/', custom_logout_view, name='logout'),  # Logout personalizado
    path('home/', homeView.as_view(), name='home'),  # Página inicial após o login
    path('hidratacao/', hidratacao, name='hidratacao'),
    path('sucesso/', LoginViewCustom.as_view(), name='sucesso'),  # Após o cadastro, redireciona para o login (ou ajuste conforme sua necessidade)
    path('estresse/', estresseView.as_view(), name="estresse"),
    path('historicohidratacao/', historicohidratacaoView.as_view(), name='historicohidratacao'),  # Página de histórico de hidratação
    path('acompanha_imc/', acompanha_imcView.as_view(), name= "acompanha_imc"),
    path('meupeso/', meupeso, name='meupeso'),
    path('veja_imc/', veja_imc, name='veja_imc'),
    path('tecnicaspbemestar/', tecnicaspbemestarView.as_view(), name= "tecnicaspbemestar"),
    path('relaxamentomuscular/', relaxamentomuscularView.as_view(), name= "relaxamentomuscular"),
    path('respiracaoguiada', respiracaoguiadaView.as_view(), name= "respiracaoguiada"),
    path('alongamento/', alongamentoView.as_view(), name= "alongamento"),
]