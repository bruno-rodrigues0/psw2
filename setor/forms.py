from django import forms
from .models import Setor

class SetorForm(forms.ModelForm):
    class Meta:
        model = Setor
        fields = ['nome', 'depto']
        labels = {
            'nome': 'Nome do Setor',
            'depto': 'Departamento',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome do Setor'}),
            'depto': forms.Select(),
        }