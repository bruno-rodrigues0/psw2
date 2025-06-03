from django import forms
from django.contrib.auth import forms as auth_forms

from . import models
    
class PessoaCreationForm(auth_forms.UserCreationForm):
    class Meta:
        model = models.Pessoa
        fields = ['nome', 'email', 'idade', 'cpf', 'telefone', 'setores', 'username', 'password1', 'password2']
        labels = {
            'nome': 'Nome',
            'email': 'Email',
            'idade': 'Idade',
            'cpf': 'CPF',
            'telefone': 'Telefone',
            'setores': 'Setores',
        }  
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'idade': forms.NumberInput(attrs={'placeholder': 'Idade'}),
            'cpf': forms.TextInput(attrs={'placeholder': 'CPF'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'Telefone'}),
            'setores': forms.SelectMultiple(attrs={'placeholder': 'Setores'}),
        }
        
class PesssoaChangeForml(auth_forms.UserChangeForm):
    class Meta:
        model = models.Pessoa
        fields = ['nome', 'email', 'idade', 'cpf', 'telefone', 'setores']
        labels = {
            'nome': 'Nome',
            'email': 'Email',
            'idade': 'Idade',
            'cpf': 'CPF',
            'telefone': 'Telefone',
            'setores': 'Setores',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'idade': forms.NumberInput(attrs={'placeholder': 'Idade'}),
            'cpf': forms.TextInput(attrs={'placeholder': 'CPF'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'Telefone'}),
            'setores': forms.SelectMultiple(attrs={'placeholder': 'Setores'}),
        }