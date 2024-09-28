from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Hidratacao
from django.contrib.auth.forms import AuthenticationForm

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

        