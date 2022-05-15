from django.db import models
from cpf_field.models import CPFField
# Create your models here.

class pessoa(models.Model):
    id_pessoa = models.IntegerField()
    vinculo = models.CharField(max_length=20)
    #id_user = user.id_user
    cpf = CPFField('cpf')
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=16)
    email = models.CharField(max_length=200)
    id_endereco = models.IntegerField()
    id_conta = models.IntegerField()
    
    def __str__(self):
        return self.email

class user(models.Model):
    id_user = models.IntegerField()
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.username

class cidade(models.Model):
    id_cidade = models.IntegerField()
    nome_cidade = models.CharField(max_length=50)
    id_uf = models.IntegerField()

    def __str__(self):
        return self.nome_cidade

class ocorrencia(models.Model):
    id_ocorrencia = models.IntegerField()
    data = models.DateField(blank=True, null=True)
    realizada = models.CharField(max_length=1)
    #ocorrencia = Clob
    id_pessoa = models.IntegerField()

    def __str__(self):
        return self.realizada

class uf(models.Model):
    id_uf = models.IntegerField()
    nome_uf = models.CharField(max_length=30)
    sigla_uf = models.CharField(max_length=2)

class endereco(models.Model):
    id_endereco = models.IntegerField()
    id_cidade = models.IntegerField()
    logradouro = models.CharField(max_length=150)
    numero = models.CharField(max_length=8)
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=80)
    complemento = models.CharField(max_length=60)
    #observacoes = clob

class conta(models.Model):
    id_conta = models.IntegerField()
    tp_conta = models.CharField(max_length=30)
    id_banco = models.IntegerField()
    banco = models.CharField(max_length=50)
    conta = models.IntegerField()
    agencia = models.IntegerField()
    operacao = models.IntegerField()