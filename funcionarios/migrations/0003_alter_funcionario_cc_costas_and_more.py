# Generated by Django 4.2.16 on 2024-10-25 11:05

from django.db import migrations, models
import funcionarios.models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0002_funcionario_cc_costas_funcionario_cc_frente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='cc_costas',
            field=models.ImageField(blank=True, null=True, upload_to=funcionarios.models.upload_to_cc),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='cc_frente',
            field=models.ImageField(blank=True, null=True, upload_to=funcionarios.models.upload_to_cc),
        ),
    ]
