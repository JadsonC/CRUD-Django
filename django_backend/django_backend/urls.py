from django import views
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from projeto.api import viewsets as projetoviewsets

route = routers.DefaultRouter()

route.register(r'users', projetoviewsets.userViewSet, basename="Users")
route.register(r'contas', projetoviewsets.contaViewSet, basename="Contas")
route.register(r'ufs', projetoviewsets.ufViewSet, basename="Ufs")
route.register(r'enderecos', projetoviewsets.enderecoViewSet, basename="Endereços")
route.register(r'pessoas', projetoviewsets.pessoaViewSet, basename="Pessoas")
route.register(r'ocorrencias', projetoviewsets.ocorrenciaViewSet, basename="Ocorrencias")
route.register(r'cidades', projetoviewsets.cidadeViewSet, basename="Cidades")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', include('projeto.urls')),
    path('', include(route.urls)),
]
