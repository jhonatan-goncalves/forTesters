from django import forms
from .models import Cenario, Projeto, Roteiro

class CenarioForm(forms.ModelForm):
    class Meta:
        model = Cenario
        fields = ('nome', 'descricao','criticidade','resultado_esperado','resultado_obtido')
