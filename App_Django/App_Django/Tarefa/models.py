from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Categoria(models.Model):
    nome = models.CharField(max_length=100,verbose_name='Nome')
    descricao = models.TextField(verbose_name='Descrição')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class TarefaManeger(models.Manager):
    def search(self,query,request):
        return self.get_queryset().filter(models.Q(user=request.user) & (models.Q(nome__contains=query ) | models.Q(descricao__contains=query ) | models.Q(categoria__nome__contains=query ) ))

class Tarefa(models.Model):

    PRIORIDADE_CHOICES = (
        ("B","Baixa"),
        ("M", "Media"),
        ("A", "Alta"),
    )

    STATUS_CHOICES = (
        ("CANC","Cancelada"),
        ("CONC","Concluida"),

    )

    nome = models.CharField(u"Nome",max_length=100)
    descricao = models.TextField(u"Descrição",blank=True)
    date = models.DateField(u"Data final")
    prioridade = models.CharField(u"Prioridade",blank=True,max_length=1, choices=PRIORIDADE_CHOICES)
    categoria = models.ForeignKey(Categoria,verbose_name='Categoria',on_delete= models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(u"Status",max_length=5,choices=STATUS_CHOICES,blank=True,default="")

    objects = TarefaManeger()

    def __str__(self):
        return self.nome
