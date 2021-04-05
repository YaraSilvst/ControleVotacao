from django import forms
from cadastro.models import *

class PessoaForm(forms.ModelForm):
    class Meta: 
        model = Pessoa
        fields = [
            "nome_completo", "cpf", "data_nascimento",
        ]

        error_messages = {
            "nome_completo": {
                "required": "O nome completo do visitante é obrigatório para o registro"
            },

            "cpf": {
                "required": "O cpf do visitante é obrigatório para o registro"
            },

            "data_nascimento": {
                "required": "A data de nascimento do visitante é obrigatória para o registro",
                "invalid": "Por favor, informe um formato válido para a data de nascimento (DD/MM/AAAA)"
            }

        }

class VotacaoForm(forms.ModelForm):
    class Meta:
        model = Votacao
        fields = [
            "nome", "descricao", "anonimo", "voto_unico", "data_inicio", "data_termino"
        ]

        error_messages = {
            "nome": {
                "required": "O nome da votação é obrigatório para o registro"
            },

            "descricao": {
                "required": "A descrição é obrigatória para o resgistro"
            },
        }

class OpcaoVotoForm(forms.ModelForm):
    class Meta:
        model = OpcaoVoto
        fields = [
            "nome", "votacao", "codigo"
        ] 

        error_messages = {
            "nome": {
                "required": "O nome para opcão de voto é obrigatório para o registro"
            },

            "votacao": {
                "required": "A votação é obrigatória para o registro"
            },

            "codigo": {
                "required": "O código é obrigatório para o resgistro"
            }
        }

