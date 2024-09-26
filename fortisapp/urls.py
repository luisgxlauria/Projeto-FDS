from django.urls import path
from .views import PaginaInicialView, cadastroView, loginView, homeView, hidratacaoView

urlpatterns = [
    path('', PaginaInicialView.as_view(), name="PaginaInicial"),
    path('cadastro/', cadastroView, name='cadastro'),
    path('login/', loginView.as_view(), name="login"),
    path('home/', homeView.as_view(), name="home"),
    path('hidratacao/', hidratacaoView.as_view(), name="hidratacao"),
    path('sucesso/', loginView.as_view(), name='sucesso'), 
]