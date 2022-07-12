from rest_framework import viewsets
from projeto.api import serializers
from projeto import models

class userViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.userSerializer
    queryset = models.user.objects.all()

class contaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.contaSerializer
    queryset = models.conta.objects.all()

class ufViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ufSerializer
    queryset = models.uf.objects.all() 

class cidadeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.cidadeSerializer
    queryset = models.cidade.objects.all()

class enderecoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.enderecoSerializer
    queryset = models.endereco.objects.all()

class pessoaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.pessoaSerializer
    queryset = models.pessoa.objects.all()

class ocorrenciaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ocorrenciaSerializer
    queryset = models.ocorrencia.objects.all()