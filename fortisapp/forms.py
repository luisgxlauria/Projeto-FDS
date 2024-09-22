from django import forms

class CadastroForm(forms.Form):
    nome = forms.CharField(max_length=100, label='Nome')
    cpf = forms.CharField(max_length=14, label='CPF')  # Formato: XXX.XXX.XXX-XX
    email = forms.EmailField(label='Email')
    senha = forms.CharField(widget=forms.PasswordInput, label='Senha')
