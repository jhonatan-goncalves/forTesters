from django.conf import settings
from django.db import models
from django.utils import timezone


class Projeto(models.Model):
    
    STATUSP_CHOICES = (
        ("ED", "Em Desenvolvimento"),
        ("EH", "Em Homologação"),
        ("F", "Finalizado"),
        ("NI", "Não Iniciado")
    )

    responsavel = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Responsável")
    nome = models.CharField("Nome", max_length=200)
    descricao = models.TextField("Descrição")
    status = models.CharField("Status", max_length=2, choices=STATUSP_CHOICES, blank=False, null=False)
    data_criacao = models.DateTimeField(default=timezone.now)

    def criacao(self):
        self.data_criacao = timezone.now()
        self.save()

    def __str__(self):
        return self.nome

class Cenario(models.Model):
    CRITICIDADE_CHOICES = ( 
        ("A", "Alta"),
        ("B", "Baixa"),
        ("M", "Média"),
        ("AL", "Altíssima"),
        ("BX", "Baixíssima")
    )
    
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    criticidade = models.CharField("Criticidade", max_length=2, choices=CRITICIDADE_CHOICES, blank=False, null=False)
    resultado_esperado = models.TextField()
    resultado_obtido = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)


class Roteiro(models.Model):
    
    STATUSR_CHOICES = (
        ("A", "Aprovado"),
        ("ET", "Em Teste"),
        ("R", "Reprovado"),
    )

    responsavel = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    status = models.CharField("Status",max_length=2, choices=STATUSR_CHOICES, blank=False, null=False)
    projetos = models.ManyToManyField(Projeto)
    cenarios = models.ManyToManyField(Cenario)
    data_criacao = models.DateTimeField(default=timezone.now)
 