from django.urls import path
from . import views  # Importa o arquivo views.py que está na mesma pasta

# Lista de caminhos deste aplicativo
urlpatterns = [
    # path(caminho, view_que_responde, nome_interno)
    # O caminho vazio '' significa: "quando entrar na raiz do site, use a view index"
    path('', views.index, name='index'),
]