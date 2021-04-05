from django.shortcuts import render, redirect
from django.contrib import messages
from cadastro.models import *
from cadastro.forms import *


def index(request):

    return render(request, "index.html")



def registrar_pessoa(request):

    form = PessoaForm()

    if request.method == "POST":
        form = PessoaForm(request.POST)

        if form.is_valid():
            pessoa = form.save(commit=False)

            pessoa.save()

            messages.success(request, "Pessoa registrada com sucesso.")

            return redirect("index")

    context = {
        "nome_pagina": "Registrar Pessoa",
        "form": form
    }

    return render(request, "registrar_pessoa.html", context)


def registrar_votacao(request):

    form = VotacaoForm()

    if request.method == "POST":
        form = VotacaoForm(request.POST)

        if form.is_valid():
            votacao = form.save(commit=False)

            votacao.save()

            messages.success(request, "Votação registrada com sucesso.")

            return redirect("index")

    context = {
        "nome_pagina": "Registrar Votação",
        "form": form
    }

    return render(request, "registrar_votacao.html", context)


def registrar_opvoto(request):

    form = OpcaoVotoForm()

    if request.method == "POST":
        form = OpcaoVotoForm(request.POST)

        if form.is_valid():
            opvoto = form.save(commit=False)

            opvoto.save()

            messages.success(request, "Opcão de voto registrada com sucesso.")

            return redirect("index")

    context = {
        "nome_pagina": "Registrar Opção de Voto",
        "form": form
    }

    return render(request, "registrar_opvoto.html", context)

def index(request):

    pessoas = Pessoa.objects.all()
    context = {
        "nome_pagina": "Controle Votação",
        "pessoas": pessoas
    }
    print(context)
    return render(request, "index.html", context)