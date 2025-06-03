from django.db import models

class Setor(models.Model):
    nome = models.CharField(max_length=100)
    depto = models.ForeignKey('depto.Depto', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome
    