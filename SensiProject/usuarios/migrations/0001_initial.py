# Generated by Django 2.0.7 on 2018-07-22 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, verbose_name='Nome do Usuário')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('telefone', models.IntegerField(verbose_name='Telefone')),
                ('chat_id', models.IntegerField(verbose_name='ID Telegram')),
            ],
        ),
    ]