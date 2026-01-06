from django.contrib import admin
from .models import Equipamento, Reuniao

# Register your models here.

# CONFIGURAÇÃO DO INVENTÁRIO NO PAINEL
@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    # Colunas que aparecem na lista
    list_display = ('nome', 'tipo', 'patrimonio', 'disponivel')
    
    # Adiciona uma barra de pesquisa
    search_fields = ('nome', 'patrimonio')
    
    # Adiciona filtros laterais
    list_filter = ('tipo', 'disponivel')

    # CONFIGURAÇÃO DAS REUNIÕES NO PAINEL
@admin.register(Reuniao)
class ReuniaoAdmin(admin.ModelAdmin):
    # Colunas que aparecem na lista
    list_display = ('data_reuniao', 'hora_inicio', 'titulo', 'status', 'tecnico_responsavel')
    
    # Filtros para encontrar reuniões passadas ou canceladas
    list_filter = ('status', 'data_reuniao')
    
    # Pesquisa por título ou nome do solicitante
    search_fields = ('titulo', 'solicitante')