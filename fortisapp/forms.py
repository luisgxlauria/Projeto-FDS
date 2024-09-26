from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

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