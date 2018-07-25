# Generated by Django 2.0.2 on 2018-03-31 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tarefa', '0002_auto_20180331_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição')),
                ('date', models.DateField(verbose_name='Data final')),
                ('prioridade', models.CharField(blank=True, choices=[('B', 'Baixa'), ('M', 'Media'), ('A', 'Alta')], max_length=1, verbose_name='Prioridade')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tarefa.Categoria', verbose_name='Categoria')),
            ],
        ),
    ]