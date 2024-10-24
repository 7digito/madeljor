from django import forms
from .models import Fornecedor

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = [
            'nome', 
            'nif', 
            'morada', 
            'morada_secundaria', 
            'codigo_postal', 
            'localidade', 
            'pais', 
            'telefone', 
            'email', 
            'www', 
            'ativo', 
            'eticadata'
        ]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control rounded'}),
            'nif': forms.TextInput(attrs={'class': 'form-control rounded'}),
            'morada': forms.TextInput(attrs={'class': 'form-control rounded'}),
            'morada_secundaria': forms.TextInput(attrs={'class': 'form-control rounded'}),
            'codigo_postal': forms.TextInput(attrs={'class': 'form-control rounded'}),
            'localidade': forms.TextInput(attrs={'class': 'form-control rounded'}),
            'pais': forms.TextInput(attrs={'class': 'form-control rounded'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control rounded'}),
            'email': forms.EmailInput(attrs={'class': 'form-control rounded'}),
            'www': forms.URLInput(attrs={'class': 'form-control rounded'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'eticadata': forms.NumberInput(attrs={'class': 'form-control rounded'}),
        }
