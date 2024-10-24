from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q  # Importa Q para consultas complexas
from .models import Fornecedor
from .forms import FornecedorForm

def fornecedor_list(request):
    query = request.GET.get('q', '')  # Captura a consulta de pesquisa, com valor padrão vazio
    # Filtra os fornecedores com base na consulta
    if query:
        fornecedores_list = Fornecedor.objects.filter(
            Q(nome__icontains=query) |
            Q(nif__icontains=query) |
            Q(telefone__icontains=query) |
            Q(email__icontains=query)
        )
    else:
        fornecedores_list = Fornecedor.objects.all()

    paginator = Paginator(fornecedores_list, 10)  # 10 fornecedores por página
    page_number = request.GET.get('page')
    fornecedores = paginator.get_page(page_number)

    return render(request, 'fornecedores/fornecedor_list.html', {
        'fornecedores': fornecedores,  # Consistência no nome
        'query': query
    })

def fornecedor_create(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fornecedor_list')
    else:
        form = FornecedorForm()
    return render(request, 'fornecedores/fornecedor_form.html', {'form': form})

def fornecedor_update(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    if request.method == 'POST':
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect('fornecedor_list')
    else:
        form = FornecedorForm(instance=fornecedor)
    return render(request, 'fornecedores/fornecedor_form.html', {'form': form})

def fornecedor_delete(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    if request.method == 'POST':
        fornecedor.delete()
        return redirect('fornecedor_list')
    return render(request, 'fornecedores/fornecedor_confirm_delete.html', {'fornecedor': fornecedor})
