import os
from django.db import models
from django.utils.text import slugify
from datetime import datetime

def upload_to_cc(instance, filename):
    # Obtém a extensão do arquivo
    ext = filename.split('.')[-1]
    # Cria um nome de arquivo único com o nome do funcionário e data atual
    filename = f"{slugify(instance.nome)}-{datetime.now().strftime('%Y%m%d%H%M%S')}.{ext}"
    # Define o caminho da pasta base/funcionarios
    return os.path.join('base/funcionarios/', filename)

class Funcionario(models.Model):
    CATEGORIAS = [
        ('gerente', 'Gerente'),
        ('administrativo', 'Administrativo'),
        ('serralheiro', 'Serralheiro'),
        ('aprendiz_serralheiro', 'Aprendiz de Serralheiro'),
        ('fiel_armazem', 'Fiel de Armazém'),
        ('engenharia', 'Engenharia'),
        ('tecnico', 'Técnico'),
    ]

    nome = models.CharField(max_length=100)
    morada = models.CharField(max_length=255, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    data_entrada = models.DateField(blank=True, null=True)  # Data de entrada na empresa
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)  # Escolha da categoria
    ativo = models.BooleanField(default=True)  # Campo ativo
    eticadata = models.IntegerField()
    eticadata_armazem = models.CharField(max_length=10, blank=True, null=True)  # Campo opcional para o armazém
    
    # Campos para as imagens do cartão de cidadão com o caminho personalizado
    cc_frente = models.ImageField(upload_to=upload_to_cc, blank=True, null=True)
    cc_costas = models.ImageField(upload_to=upload_to_cc, blank=True, null=True)

    def __str__(self):
        return self.nome
