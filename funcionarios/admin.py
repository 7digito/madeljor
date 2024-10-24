from django.contrib import admin
from .models import Funcionario

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'data_entrada', 'categoria', 'ativo')
    search_fields = ('nome', 'telefone', 'categoria')
    list_filter = ('categoria', 'ativo')
