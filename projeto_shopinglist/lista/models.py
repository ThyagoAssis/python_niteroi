from django.db import models

# Create your models here.
class Alunos(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False )
    curso = models.CharField(max_length=100, null=False, blank=False )
    turma = models.CharField(max_length=100, null=False, blank=False)