from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class Usuario(AbstractUser):
    cpf = models.CharField(max_length=14, unique=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
class Hidratacao(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Associa ao usuário logado
    quantidade_agua = models.PositiveIntegerField()  # Armazena a quantidade de água ingerida em ml
    data_hora = models.DateTimeField(auto_now_add=True)  # Registra automaticamente a data e hora do registro

    def __str__(self):
        return f"{self.usuario.username} - {self.quantidade_agua}ml em {self.data_hora}"