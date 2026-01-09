from django.shortcuts import render, redirect
from .models import Reuniao  # Importamos nosso modelo de Reuniões
from .forms import ReuniaoForm

# Create your views here.

def index(request):
    reunioes = Reuniao.objects.all()
    contexto = {
        'reunioes': reunioes
    }
    return render(request, 'index.html', contexto)

def destino_login(request):
    # Verifica se o usuario tem crachá de Admin
    if request.user.is_superuser:
        return redirect('/admin/')  # Manda para o painel administrativo
    else:
        return redirect('index')    # Manda para a pagina inicial
    
def criar_reuniao(request):
    if request.method == 'POST':
        forms = ReuniaoForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('index')
    else:
        forms = ReuniaoForm()

    return render(request, 'reuniao_form.html', {'form': forms})