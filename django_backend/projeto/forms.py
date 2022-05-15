from django import forms

from django_backend.projeto.models import pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model = pessoa
        fields = '__all__'
        