from django.contrib import admin

# Register your models here.

from projeto.models import cidade
from projeto.models import ocorrencia
from projeto.models import pessoa
from projeto.models import user
from projeto.models import uf
from projeto.models import endereco
from projeto.models import conta

admin.site.register(cidade)
admin.site.register(ocorrencia)
admin.site.register(pessoa)
admin.site.register(user)
admin.site.register(uf)
admin.site.register(endereco)
admin.site.register(conta)