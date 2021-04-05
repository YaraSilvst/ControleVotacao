from django.shortcuts import render, redirect

from cadastro.models import *
from adm.models import *
import datetime
from django.utils import timezone


def home_view(request):
    today = datetime.date.today()
    print(today)
    
    objVotacoes = Votacao.objects.filter(data_inicio__lte=today, data_termino__gte=today)
    
    context = {
        "listVotacoes": objVotacoes,
    }

    return render(request, "index.html", context)
