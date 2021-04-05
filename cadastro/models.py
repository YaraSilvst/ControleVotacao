from django.db import models

class Pessoa(models.Model):

    nome_completo = models.CharField(
        verbose_name = "Nome completo",
        max_length = 194,
    )

    cpf = models.CharField(
        verbose_name = "CPF",
        max_length = 14,
        unique=True,
    )

    data_nascimento = models.DateField(
        verbose_name = "Data de nascimento",
        auto_now = False,
        auto_now_add = False,
    )

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
        db_table = "pessoa"

    def __str__(self):
        return self.nome_completo



class Votacao(models.Model):

    nome = models.CharField(
        verbose_name = "Nome",
        max_length = 194,
    )

    descricao = models.CharField(
        verbose_name = "Descrição",
        max_length = 194,
    )

    anonimo = models.BooleanField(
        verbose_name = "Anônimo",
        unique = False,
    )

    voto_unico = models.BooleanField(
        verbose_name = "Voto Único",
        unique = False,
    )

    data_inicio = models.DateField(
        verbose_name = "Data Início",
        auto_now = False,
        auto_now_add = False,
    )

    data_termino = models.DateField(
        verbose_name = "Data Término",
        auto_now = False,
        auto_now_add = False
    )

    class Meta:
        verbose_name = "Votação"
        verbose_name_plural = "Votações"
        db_table = "votacao"

    def __str__(self):
        return self.nome



class OpcaoVoto(models.Model):

    nome = models.CharField(
        verbose_name = "Nome",
        max_length = 194,
    )

    votacao = models.ForeignKey(Votacao, on_delete=models.CASCADE)

    codigo = models.CharField(
        verbose_name = "Código",
        max_length = 5,
    )

    numero_votos = models.IntegerField(
        verbose_name = "Número Votos",
        default=0,
    )

    class Meta:
        verbose_name = "Opção de voto"
        verbose_name_plural = "Opções de voto"
        db_table = "opcaovoto"

    def __str__(self):
        return self.nome

