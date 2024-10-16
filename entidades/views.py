from django.shortcuts import render
from .models import Cliente


# Create your views here.

def lista_clientes(request):
    # Lógica para listar clientes
    return render(request, 'entidades/lista_clientes.html', {})