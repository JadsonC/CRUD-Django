from rest_framework import serializers
from projeto import models

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.user
        fields = '__all__'

class contaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.conta
        fields = '__all__'

class ufSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.uf
        fields = '__all__'   

class cidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.cidade
        fields = '__all__'

class enderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.endereco
        fields = '__all__'  

class pessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.pessoa
        fields = '__all__'

class ocorrenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ocorrencia
        fields = '__all__'