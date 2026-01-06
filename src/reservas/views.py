from django.shortcuts import render
from .models import Reuniao  # Importamos nosso modelo de Reuniões

# Create your views here.

def index(request):
    # BUSCA DE DADOS
    # O comando .all() pega todas as linhas da tabela de reuniões no banco
    reunioes = Reuniao.objects.all()
    
    # PACOTE DE DADOS
    # Criamos um dicionário (contexto) para enviar esses dados para o HTML
    contexto = {
        'reunioes': reunioes
    }
    
    # RESPOSTA VISUAL
    # Renderiza (desenha) o arquivo HTML usando os dados do contexto
    return render(request, 'index.html', contexto)