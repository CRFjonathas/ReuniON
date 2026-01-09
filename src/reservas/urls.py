from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('redirecionar/', views.destino_login, name='destino_login'),
]