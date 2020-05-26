from django import forms
from .models import Cenario, Projeto, Roteiro

class CenarioForm(forms.ModelForm):
    class Meta:
        model = Cenario
        fields = ('nome', 'descricao','criticidade','resultado_esperado','resultado_obtido')

class RoteiroForm(forms.ModelForm):
    class Meta:
        model = Roteiro
        fields = ('responsavel', 'nome', 'descricao', 'status', 'projetos', 'cenarios', 'data_criacao')

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ('responsavel', 'nome', 'descricao', 'status', 'data_criacao')
