from django.urls import path
from .views import *

urlpatterns = [
    path('votar/<int:id_votacao>/<int:id_pessoa>/', votar, name="votar"),
    path('validar/<int:id_votacao>/', validacao, name="validar"),
    path('apuracao_votos/<int:id_votacao>/', apuracao_votos, name="apuracao_votos"),
]