from django.db import models
from cpf_field.models import CPFField
# Create your models here.

class user(models.Model):
    id_user = models.IntegerField()
    user_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.user_name)    

class conta(models.Model):
    id_conta = models.IntegerField()
    tp_conta = models.CharField(max_length=30)
    id_banco = models.IntegerField()
    banco = models.CharField(max_length=50)
    conta = models.IntegerField()
    agencia = models.IntegerField()
    operacao = models.IntegerField()

    def __str__(self):
        return str(self.conta)

class uf(models.Model):
    id_uf = models.IntegerField()
    nome_uf = models.CharField(max_length=30)
    sigla_uf = models.CharField(max_length=2)

    def __str__(self):
        return str(self.nome_uf)    

class cidade(models.Model):
    id_cidade = models.IntegerField()
    nome_cidade = models.CharField(max_length=50)
    id_uf = models.ForeignKey(uf, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.nome_cidade)

class endereco(models.Model):
    id_endereco = models.IntegerField()
    id_cidade = models.ForeignKey(cidade, on_delete=models.PROTECT)
    logradouro = models.CharField(max_length=150)
    numero = models.CharField(max_length=8)
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=80)
    complemento = models.CharField(max_length=60)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.logradouro)    

class pessoa(models.Model):
    id_pessoa = models.IntegerField()
    vinculo = models.CharField(max_length=20)
    id_user = models.ForeignKey(user, on_delete=models.PROTECT, blank=True, null=True)
    cpf = CPFField('cpf')
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=16)
    email = models.CharField(max_length=200)
    id_endereco = models.ForeignKey(endereco, on_delete=models.PROTECT)
    id_conta = models.ForeignKey(conta, on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.nome)

class ocorrencia(models.Model):
    id_ocorrencia = models.IntegerField()
    data = models.DateField(blank=True, null=True)
    realizada = models.CharField(max_length=1)
    ocorrencia = models.TextField(blank=True, null=True)
    id_pessoa = models.ForeignKey(pessoa, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.data)
