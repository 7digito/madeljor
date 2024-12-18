from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q  # Importa Q para consultas complexas
from .models import Cliente
from .forms import ClienteForm

def cliente_list(request):
    query = request.GET.get('q')
    if query:
        clientes_list = Cliente.objects.filter(
            Q(nome__icontains=query) |
            Q(nif__icontains=query) |
            Q(telefone__icontains=query) |
            Q(email__icontains=query)
        ).order_by('nome')
    else:
        clientes_list = Cliente.objects.all().order_by('nome')

    # Debugging
    print(f'Total de clientes: {clientes_list.count()}')  
    print(f'Query: {query}')  

    paginator = Paginator(clientes_list, 10)
    page_number = request.GET.get('page')
    clientes = paginator.get_page(page_number)

    print(f'Clientes na página: {clientes.object_list.count()}')  # Adicionando contagem de clientes na página
    print(f'Página atual: {clientes.number}')  

    return render(request, 'mdj_clientes/cliente_list.html', {'clientes': clientes, 'query': query})


def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'mdj_clientes/cliente_form.html', {'form': form})

def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'mdj_clientes/cliente_form.html', {'form': form})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'mdj_clientes/cliente_confirm_delete.html', {'cliente': cliente})
