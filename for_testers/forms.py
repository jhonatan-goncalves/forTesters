from django import forms
from .models import Cenario, Projeto, Roteiro


class CenarioForm(forms.ModelForm):
    class Meta:
        model = Cenario
        fields = ('nome', 'descricao', 'criticidade','resultado_esperado', 'resultado_obtido')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'size': 37.5, 'title': 'Nome do Cenário'})


class RoteiroForm(forms.ModelForm):
    class Meta:
        model = Roteiro
        fields = ('responsavel', 'nome', 'status','descricao','projetos', 'cenarios', 'data_criacao')
        

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ('responsavel', 'nome','status', 'descricao', 'data_criacao')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['responsavel'].widget.attrs.update({'title': 'Responsável pelo Projeto'})
        self.fields['nome'].widget.attrs.update({'size': 37.5, 'title': 'Nome do Projeto'})
        self.fields['data_criacao'].widget.attrs.update({'size': 37.5, 'title': 'Data de criação do Projeto'})
