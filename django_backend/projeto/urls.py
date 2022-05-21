from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('pessoas/', views.pessoa_modelform, name='pessoa_modelform'),
    path('cidades/', views.cidade_modelform, name='cidade_modelform'),
    path('usuarios/', views.user_modelform, name='user_modelform'),
    path('ocorrencias/', views.ocorrencia_modelform, name='ocorrencia_modelform'),
    path('enderecos/', views.endereco_modelform, name='endereco_modelform'),
    path('ufs/', views.uf_modelform, name='uf_modelform'),
    path('contas/', views.conta_modelform, name='conta_modelform'),
    path('', views.menu, name='menu'),
]