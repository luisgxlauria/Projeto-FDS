from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    cpf = models.CharField(max_length=14, unique=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username