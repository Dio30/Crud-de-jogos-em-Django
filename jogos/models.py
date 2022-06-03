from turtle import width
from django.db import models
from django.contrib.auth.models import User

class Jogos(models.Model):
    nome_do_jogo = models.CharField(max_length=30)
    tipo_de_jogo = models.CharField(max_length=30)
    valor_do_jogo = models.DecimalField(max_digits=7, decimal_places=2)
    descrição_do_jogo = models.CharField(max_length=100, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'
        ordering = ['nome_do_jogo',]
    
    def __str__(self):
        return self.nome_do_jogo