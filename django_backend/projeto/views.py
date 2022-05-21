from msilib.schema import Class
from pipes import Template
from django.shortcuts import render

from projeto.forms import UfFormulario
from projeto.forms import EnderecoFormulario
from projeto.forms import ContaFormulario
from projeto.forms import CidadeFormulario
from projeto.forms import PessoaFormulario
from projeto.forms import UserFormulario
from projeto.forms import OcorrenciaFormulario

# Create your views here.

def pessoa_modelform(request):
    if request.method == "GET":
        form = PessoaFormulario()
        context = {
            'form': form
        }
        return render(request, "formularios/pessoa_modelform.html", context=context)
    
    else:
        form = PessoaFormulario(request.POST)
        if form.is_valid():
            pessoa = form.save()
            form = PessoaFormulario()

        context = {
            'form': form
        }
        return render(request, "formularios/pessoa_modelform.html", context=context)
            
def cidade_modelform(request):
    if request.method == "GET":
        form = CidadeFormulario()
        context = {
            'form': form
        }
        return render(request, "formularios/cidade_modelform.html", context=context)
    
    else:
        form = CidadeFormulario(request.POST)
        if form.is_valid():
            cidade = form.save()
            form = CidadeFormulario()

        context = {
            'form': form
        }
        return render(request, "formularios/cidade_modelform.html", context=context)

def user_modelform(request):
    if request.method == "GET":
        form = UserFormulario()
        context = {
            'form': form
        }
        return render(request, "formularios/user_modelform.html", context=context)
    
    else:
        form = UserFormulario(request.POST)
        if form.is_valid():
            user = form.save()
            form = UserFormulario()

        context = {
            'form': form
        }
        return render(request, "formularios/user_modelform.html", context=context)

def conta_modelform(request):
    if request.method == "GET":
        form = ContaFormulario()
        context = {
            'form': form
        }
        return render(request, "formularios/conta_modelform.html", context=context)
    
    else:
        form = ContaFormulario(request.POST)
        if form.is_valid():
            conta = form.save()
            form = ContaFormulario()

        context = {
            'form': form
        }
        return render(request, "formularios/conta_modelform.html", context=context)

def endereco_modelform(request):
    if request.method == "GET":
        form = EnderecoFormulario()
        context = {
            'form': form
        }
        return render(request, "formularios/endereco_modelform.html", context=context)
    
    else:
        form = EnderecoFormulario(request.POST)
        if form.is_valid():
            endereco = form.save()
            form = EnderecoFormulario()

        context = {
            'form': form
        }
        return render(request, "formularios/endereco_modelform.html", context=context)

def ocorrencia_modelform(request):
    if request.method == "GET":
        form = OcorrenciaFormulario()
        context = {
            'form': form
        }
        return render(request, "formularios/ocorrencia_modelform.html", context=context)
    
    else:
        form = OcorrenciaFormulario(request.POST)
        if form.is_valid():
            ocorrencia = form.save()
            form = OcorrenciaFormulario()

        context = {
            'form': form
        }
        return render(request, "formularios/ocorrencia_modelform.html", context=context)

def uf_modelform(request):
    if request.method == "GET":
        form = UfFormulario()
        context = {
            'form': form
        }
        return render(request, "formularios/uf_modelform.html", context=context)
    
    else:
        form = UfFormulario(request.POST)
        if form.is_valid():
            user = form.save()
            form = UfFormulario()

        context = {
            'form': form
        }
        return render(request, "formularios/uf_modelform.html", context=context)

def menu(request):
    return render(request, "menu_principal/menu.html")