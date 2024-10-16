from django import forms
from .models import Cliente
from .models import Fornecedor

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'nif', 'telefone', 'email', 'morada', 'localidade', 'codigo_postal', 'website']

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'nif', 'telefone', 'email', 'morada', 'localidade', 'codigo_postal', 'website']

