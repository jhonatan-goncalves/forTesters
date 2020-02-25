from django.conf import settings
from django.db import models
from django.utils import timezone


class Projeto(models.Model):
    responsavel = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    data_inicio = models.DateTimeField(default=timezone.now)
    data_criacao = models.DateTimeField(blank=True, null=True)

    def criacao(self):
        self.data_criacao = timezone.now()
        self.save()

    def __str__(self):
        return self.nome