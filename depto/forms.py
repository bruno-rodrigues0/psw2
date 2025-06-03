from django import forms
from .models import Depto

class DeptoForm(forms.ModelForm):
    class Meta:
        model = Depto
        fields = ['nome']
        labels = {
            'nome': 'Nome do Departamento',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }