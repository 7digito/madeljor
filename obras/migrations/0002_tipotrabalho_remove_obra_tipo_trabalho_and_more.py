# Generated by Django 4.2.16 on 2024-10-25 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoTrabalho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(choices=[('aluminio', 'Alumínio'), ('pvc', 'PVC'), ('vidro', 'Vidro'), ('ferro', 'Ferro'), ('aco_inox', 'Aço Inox'), ('outros', 'Outros')], max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='obra',
            name='tipo_trabalho',
        ),
        migrations.AddField(
            model_name='obra',
            name='tipo_trabalho',
            field=models.ManyToManyField(to='obras.tipotrabalho'),
        ),
    ]