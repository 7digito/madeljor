from django.db import models

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
    
    # Novos campos para as imagens do cartão de cidadão
    cc_frente = models.ImageField(upload_to='funcionarios/cc_frente/', blank=True, null=True)
    cc_costas = models.ImageField(upload_to='funcionarios/cc_costas/', blank=True, null=True)

    def __str__(self):
        return self.nome
