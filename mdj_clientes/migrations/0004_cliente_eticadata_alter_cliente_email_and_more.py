# Generated by Django 4.2.16 on 2024-10-23 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdj_clientes', '0003_rename_morada_cliente_morada1_cliente_morada2'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='eticadata',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='pais',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
