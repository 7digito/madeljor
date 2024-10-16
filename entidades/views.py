from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm
from .models import Fornecedor
from .forms import FornecedorForm


# Create your views here.

def lista_clientes(request):
    clientes = Cliente.objects.all()  # Pega todos os clientes do banco de dados
    return render(request, 'entidades/lista_clientes.html', {'clientes': clientes})

def adicionar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'entidades/adicionar_cliente.html', {'form': form})

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'entidades/editar_cliente.html', {'form': form})

def apagar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'entidades/apagar_cliente.html', {'cliente': cliente})

# Listar Fornecedores
def lista_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedores/lista_fornecedores.html', {'fornecedores': fornecedores})

# Adicionar Fornecedor
def adicionar_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_fornecedores')  # Redireciona para a lista de fornecedores
    else:
        form = FornecedorForm()
    return render(request, 'fornecedores/adicionar_fornecedor.html', {'form': form})

# Editar Fornecedor
def editar_fornecedor(request, id):
    fornecedor = get_object_or_404(Fornecedor, id=id)
    if request.method == 'POST':
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect('lista_fornecedores')  # Redireciona para a lista de fornecedores
    else:
        form = FornecedorForm(instance=fornecedor)
    return render(request, 'fornecedores/editar_fornecedor.html', {'form': form})

# Apagar Fornecedor
def apagar_fornecedor(request, id):
    fornecedor = get_object_or_404(Fornecedor, id=id)
    if request.method == 'POST':
        fornecedor.delete()
        return redirect('lista_fornecedores')  # Redireciona para a lista de fornecedores
    return render(request, 'fornecedores/apagar_fornecedor.html', {'fornecedor': fornecedor})
