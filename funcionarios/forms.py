from django import forms
from .models import Funcionario

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = [
            'nome',
            'morada',
            'telefone',
            'data_entrada',
            'categoria',
            'ativo',
            'eticadata',
            'eticadata_armazem',
            'cc_frente',  # Adicionando o campo de imagem
            'cc_costas',  # Adicionando o campo de imagem
        ]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control rounded'}),
            'morada': forms.TextInput(attrs={'class': 'form-control rounded'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control rounded'}),
            'data_entrada': forms.DateInput(attrs={'class': 'form-control rounded', 'type': 'date'}),
            'categoria': forms.Select(attrs={'class': 'form-select rounded'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'eticadata': forms.NumberInput(attrs={'class': 'form-control rounded'}),
            'eticadata_armazem': forms.TextInput(attrs={'class': 'form-control rounded'}),
            'cc_frente': forms.ClearableFileInput(attrs={'class': 'form-control rounded'}),  # Campo para imagem
            'cc_costas': forms.ClearableFileInput(attrs={'class': 'form-control rounded'}),  # Campo para imagem
        }
