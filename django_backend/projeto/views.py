from django.views.generic import ListView
from django.shortcuts import render

from django_backend.projeto.models import pessoa

# Create your views here.

class PessoaList(ListView):
    model = pessoa
    queryset: pessoa.objects.all()

