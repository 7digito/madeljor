from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    nif = models.CharField(max_length=15)
    morada = models.CharField(max_length=255)
    morada_secundaria = models.CharField(max_length=255, blank=True, null=True)  # Campo opcional
    codigo_postal = models.CharField(max_length=10)
    localidade = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    www = models.URLField(blank=True, null=True)
    ativo = models.BooleanField(default=True)  # Certifique-se de que este campo existe
    eticadata = models.IntegerField()

    def __str__(self):
        return self.nome
