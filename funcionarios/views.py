from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q  # Importa Q para consultas complexas
from .models import Funcionario
from .forms import FuncionarioForm

def funcionario_list(request):
    query = request.GET.get('q')  # Captura a consulta de pesquisa
    if query:
        # Filtra os funcionários com base na consulta
        funcionarios_list = Funcionario.objects.filter(
            Q(nome__icontains=query) |
            Q(telefone__icontains=query) |
            Q(categoria__icontains=query)
        )
    else:
        funcionarios_list = Funcionario.objects.all()

    paginator = Paginator(funcionarios_list, 10)  # 10 funcionários por página
    page_number = request.GET.get('page')
    funcionarios = paginator.get_page(page_number)

    return render(request, 'funcionarios/funcionario_list.html', {'funcionarios': funcionarios, 'query': query})

def funcionario_create(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('funcionario_list')
    else:
        form = FuncionarioForm()
    return render(request, 'funcionarios/funcionario_form.html', {'form': form})

def funcionario_update(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('funcionario_list')
    else:
        form = FuncionarioForm(instance=funcionario)
    return render(request, 'funcionarios/funcionario_form.html', {'form': form})

def funcionario_delete(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == 'POST':
        funcionario.delete()
        return redirect('funcionario_list')
    return render(request, 'funcionarios/funcionario_confirm_delete.html', {'funcionario': funcionario})

def funcionario_detail(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    return render(request, 'funcionarios/funcionario_detail.html', {'funcionario': funcionario})