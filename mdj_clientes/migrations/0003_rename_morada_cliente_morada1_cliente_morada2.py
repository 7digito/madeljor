# Generated by Django 4.2.16 on 2024-10-23 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdj_clientes', '0002_cliente_estado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='morada',
            new_name='morada1',
        ),
        migrations.AddField(
            model_name='cliente',
            name='morada2',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
