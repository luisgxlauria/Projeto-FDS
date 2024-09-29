from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Hidratacao
from django.contrib.auth.forms import AuthenticationForm
from .models import Peso
from .models import MetaPeso

class UsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nome = forms.CharField(required=True)

    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'cpf', 'username', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UsuarioForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.nome = self.cleaned_data['nome']
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Nome de Usuário',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome de usuário'})
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'})
    )

class HidratacaoForm(forms.ModelForm):
    class Meta:
        model = Hidratacao
        fields = ['quantidade_agua'] 
        widgets = {
            'quantidade_agua': forms.NumberInput(attrs={'min': '1', 'required': True}),
        }

class PesoForm(forms.ModelForm):
    class Meta:
        model = Peso
        fields = ['peso', 'altura']  # O IMC será calculado automaticamente
        widgets = {
            'peso': forms.NumberInput(attrs={'step': '0.1', 'required': True}),
            'altura': forms.NumberInput(attrs={'step': '0.01', 'required': True}),
        }

    def save(self, commit=True):
        peso_instance = super().save(commit=False)
        peso_instance.imc = peso_instance.peso / (peso_instance.altura ** 2)  # Cálculo do IMC
        if commit:
            peso_instance.save()
        return peso_instance
    
class MetaPesoForm(forms.ModelForm):
    class Meta:
        model = MetaPeso
        fields = ['tipo_meta', 'quantidade', 'prazo']
        widgets = {
            'tipo_meta': forms.Select(attrs={'required': True}),
            'quantidade': forms.NumberInput(attrs={'step': '0.1', 'required': True}),
            'prazo': forms.DateInput(attrs={'type': 'date', 'required': True}),
        }

