from django.shortcuts import render, redirect
from django.contrib import messages

from cadastro.models import *
from datetime import datetime, timezone
from adm.models import *


def votar(request, id_votacao, id_pessoa):

    objVotacao = Votacao.objects.get(pk=id_votacao)
    objPessoa = Pessoa.objects.get(pk=id_pessoa)

    listOpcaoVoto = OpcaoVoto.objects.filter(votacao=objVotacao)

    if objVotacao.voto_unico == True and PessoaVoto.objects.filter(pessoa=objPessoa, votacao=objVotacao):
        
        messages.error(request, "Seu voto já foi computado nesta eleição.")

        return redirect('index')

    if request.POST:
        idOpcaoVoto = request.POST.get('voto', None)
        objOpcaoVoto = OpcaoVoto.objects.get(pk=idOpcaoVoto)

        objOpcaoVoto.numero_votos += 1
        objOpcaoVoto.save()
        
        try:
            objPessoa_voto = PessoaVoto.objects.get(pessoa=objPessoa, votacao=objVotacao, opcao=objOpcaoVoto)
            objPessoa_voto.numero_votos += 1

        except:
            objPessoa_voto = PessoaVoto()
            objPessoa_voto.pessoa = objPessoa
            objPessoa_voto.votacao = objVotacao
            objPessoa_voto.opcao = objOpcaoVoto
            objPessoa_voto.numero_votos += 1

        objPessoa_voto.save()

        messages.success(request, "Voto registrado com sucesso.")

        return redirect('index')

    context = {
        "objVotacao": objVotacao,
        "listOpcaoVoto": listOpcaoVoto,
    }

    return render(request, "votar.html", context)
    

def validacao(request, id_votacao):

    if request.POST:
        cpf = request.POST.get('cpf', None)
        try: 
            pessoa = Pessoa.objects.get(cpf=cpf)
            return redirect("votar", id_votacao, pessoa.id)

        except Pessoa.DoesNotExist: 
            messages.error(request, "CPF não cadastrado!")

    return render(request, "validacao.html")


def apuracao_votos(request, id_votacao):

    objVotacao = Votacao.objects.get(pk=id_votacao)
    objOpcao_Voto = OpcaoVoto.objects.filter(votacao=objVotacao)

    context = {
        "listVotacoes": objOpcao_Voto
    }

    return render(request, "apuracao.html", context)



