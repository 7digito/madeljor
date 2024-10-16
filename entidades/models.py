from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    nif = models.CharField(max_length=15, verbose_name='Número de Identificação Fiscal')
    morada = models.CharField(max_length=255, blank=True)
    codigo_postal = models.CharField(max_length=10, blank=True)
    localidade = models.CharField(max_length=100, blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    cliente_desde = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome
    
class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    nif = models.CharField(max_length=15)  # Número de identificação fiscal
    morada = models.CharField(max_length=255, blank=True)
    codigo_postal = models.CharField(max_length=10, blank=True)
    localidade = models.CharField(max_length=100, blank=True)
    telefone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.nome
