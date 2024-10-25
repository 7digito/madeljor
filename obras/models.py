from django.db import models
from mdj_clientes.models import Cliente  # Certifique-se de importar o modelo Cliente

class TipoTrabalho(models.Model):
    nome = models.CharField(max_length=25)

    def __str__(self):
        return self.nome


class Obra(models.Model):
    ESTADOS = [
        ('orçamentada', 'Orçamentada'),
        ('adjudicada', 'Adjudicada'),
        ('em preparação', 'Em Preparação'),
        ('em execução', 'Em Execução'),
        ('pendente', 'Pendente'),
        ('concluída', 'Concluída'),
        ('fechada', 'Fechada'),
        # Adicione mais estados conforme necessário
    ]

    numero_identificativo = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=100)  # Campo para o nome da obra
    local = models.CharField(max_length=200)  # Campo para o local da obra
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_trabalho = models.ManyToManyField(TipoTrabalho)  # Permite selecionar vários tipos de trabalho
    estado = models.CharField(max_length=20, choices=ESTADOS)

    def __str__(self):
        return f'{self.numero_identificativo} - {self.nome} - {self.cliente.nome}'
