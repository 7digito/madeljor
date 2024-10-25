from django import forms
from .models import Obra, TipoTrabalho

class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = ['numero_identificativo', 'nome', 'local', 'cliente', 'tipo_trabalho', 'estado']
        widgets = {
            'tipo_trabalho': forms.CheckboxSelectMultiple(),
            'estado': forms.Select(attrs={'class': 'form-control'})  # Adicionando estilo ao Select
        }
        labels = {
            'numero_identificativo': 'Número Identificativo',
            'nome': 'Nome da Obra',
            'local': 'Local da Obra',
            'cliente': 'Cliente',
            'tipo_trabalho': 'Tipos de Trabalho',
            'estado': 'Estado da Obra'
        }
