from django.db import models
from django.contrib.auth import models as auth_models

class Pessoa(auth_models.User):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    cpf = models.CharField(max_length=11, unique=True, null=True)
    telefone = models.CharField(max_length=15, null=True)
    setores = models.ManyToManyField('setor.Setor', blank=True)
    add_em = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.nome