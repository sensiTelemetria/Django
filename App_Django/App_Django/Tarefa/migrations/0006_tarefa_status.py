# Generated by Django 2.0.2 on 2018-04-27 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tarefa', '0005_categoria_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='status',
            field=models.CharField(blank=True, choices=[('CANCELADA', 'Cancelada'), ('CONCLUIDA', 'Concluida')], default='', max_length=5, verbose_name='Status'),
        ),
    ]
