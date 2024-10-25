# Generated by Django 4.2.16 on 2024-10-25 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mdj_clientes', '0007_alter_cliente_email_alter_cliente_telefone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_identificativo', models.CharField(max_length=50, unique=True)),
                ('tipo_trabalho', models.CharField(choices=[('aluminio', 'Alumínio'), ('pvc', 'PVC'), ('vidro', 'Vidro'), ('ferro', 'Ferro'), ('aco_inox', 'Aço Inox'), ('outros', 'Outros')], max_length=20)),
                ('estado', models.CharField(choices=[('orçamentada', 'Orçamentada'), ('adjudicada', 'Adjudicada'), ('em preparação', 'Em Preparação'), ('em execução', 'Em Execução'), ('pendente', 'Pendente'), ('concluída', 'Concluída')], max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mdj_clientes.cliente')),
            ],
        ),
    ]