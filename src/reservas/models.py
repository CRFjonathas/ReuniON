from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# CLASSE 1: INVENTÁRIO

class Equipamento(models.Model):
    TIPO_CHOICES = [
        ('NB', 'Notebook'),
        ('CAM', 'Câmera/Webcam'),
        ('MIC', 'Microfone'),
        ('CX', 'Caixa de Som'),
        ('CAB', 'Cabos/Adaptadores'),
        ('OUT', 'Outros'),
    ]

    # Definição das colunas da tabela
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=3, choices=TIPO_CHOICES)
    patrimonio = models.CharField(max_length=50, unique=True, verbose_name="N° Patrimônio")
    disponivel = models.BooleanField(default=True, verbose_name="Em estoque?")

    # Esta função diz como o objeto deve aparecer escrito (ex: ao invés de "Equipamento object (1)", aparece o nome)
    def __str__(self):
        return f"{self.nome} ({self.patrimonio})"
    
# CLASSE 2: REUNIÕES
class Reuniao(models.Model):
    STATUS_CHOICES = [
        ('AGENDA', 'Agendada (Pendente)'),
        ('REALIZADA', 'Realizada com Sucesso'),
        ('CANCELADA', 'Cancelada'),
    ]

    # Dados principais
    titulo = models.CharField(max_length=200, verbose_name="Assunto da Reunião")
    data_reuniao = models.DateField() 
    hora_teste = models.TimeField(verbose_name="Início do Teste")
    hora_inicio = models.TimeField(verbose_name="Início da Reunião")
    local = models.CharField(max_length=100)
    link_reuniao = models.URLField(max_length=500, blank=True, null=True)

    # Pessoas
    solicitante = models.CharField(max_length=100, help_text="Nome ou Seção")
    # ForeignKey cria um link com a tabela de Usuários. Se o usuário for deletado, o campo fica nulo (SET_NULL)
    tecnico_responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Técnico Responsável")

    equipamentos = models.ManyToManyField(Equipamento, blank=True, verbose_name="Equipamentos Utilizados")

    # Controle
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='AGENDADA')
    observacoes = models.TextField(blank=True, null=True) # Campo de texto grande (sem limite)

    # Metadados (Registros automáticos de quando foi criado/modificado)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    # Configurações extras da classe
    class Meta:
        ordering = ['data_reuniao', 'hora_inicio'] # Ordena a lista automaticamente por data e hora
        verbose_name = "Reunião"
        verbose_name_plural = "Reuniões" # Corrige erro de ortografia do Django de "Reuniaos" para "Reuniões".
    def __str__(self):
        return f"{self.data_reuniao} - {self.titulo}"