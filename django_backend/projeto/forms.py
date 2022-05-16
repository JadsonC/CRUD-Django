from django import forms

from projeto.models import pessoa, cidade, user, conta, endereco, cidade, ocorrencia, uf

class PessoaFormulario(forms.ModelForm):
    class Meta:
        model = pessoa
        fields = '__all__'

class CidadeFormulario(forms.ModelForm):
    class Meta:
        model = cidade
        fields = '__all__'

class UserFormulario(forms.ModelForm):
    class Meta:
        model = user
        fields = '__all__'

class ContaFormulario(forms.ModelForm):
    class Meta:
        model = conta
        fields = '__all__'

class EnderecoFormulario(forms.ModelForm):
    class Meta:
        model = endereco
        fields = '__all__'

class CidadeFormulario(forms.ModelForm):
    class Meta:
        model = cidade
        fields = '__all__'

class OcorrenciaFormulario(forms.ModelForm):
    class Meta:
        model = ocorrencia
        fields = '__all__'

class UfFormulario(forms.ModelForm):
    class Meta:
        model = uf
        fields = '__all__'