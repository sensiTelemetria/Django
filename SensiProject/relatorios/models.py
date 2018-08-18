from django.db import models

from tags import models as tags_models
from usuarios import models as usuarios_models


# Create your models here.
class relatorio(models.Model):
    PERIODICIDADE_CHOINCES={
        ('S','Semanal'),
        ('M','Mensal'),
        ('D','Diário'),
    }
    nome = models.CharField(max_length=20, verbose_name= 'Nome do Relatório')
    tags = models.ManyToManyField(tags_models.tag)
    usuarios = models.ManyToManyField(usuarios_models.usuario)
    periodicidade = models.CharField(max_length=1,choices=PERIODICIDADE_CHOINCES,default='M')

    def __str__(self):
        return self.nome
