from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    nif = models.CharField(max_length=15, verbose_name='Número de Identificação Fiscal')

    def __str__(self):
        return self.nome
