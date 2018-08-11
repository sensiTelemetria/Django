from django.db import models

from tags import models as tags_models
from usuarios import models as usuarios_models


# Create your models here.
class relatorio(models.Model):
    tags = models.ManyToManyField(tags_models.tag)
    usuarios = models.ManyToManyField(usuarios_models.usuario)
    inicio = models.DateField(verbose_name='Data de Início')
    fim = models.DateField(verbose_name='Data de Término')

    def __str__(self):
        return str(self.id) + ' |  de' + str(self.inicio) +' até ' + str(self.fim)
