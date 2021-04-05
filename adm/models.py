from django.db import models
from cadastro.models import *

class PessoaVoto(models.Model):

    class Meta:
        verbose_name = "Voto da Pessoa"
        verbose_name_plural = "Voto das Pessoas"
        db_table = "pessoavoto"

    pessoa = models.ForeignKey(Pessoa, on_delete = models.CASCADE, verbose_name="Pessoa")
    votacao = models.ForeignKey(Votacao, on_delete = models.CASCADE, verbose_name="Votação")
    opcao = models.ForeignKey(OpcaoVoto, on_delete = models.CASCADE, verbose_name="Opção de voto")
    numero_votos = models.IntegerField(verbose_name="Quantidade de votos", default = 0)