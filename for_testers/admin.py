from django.contrib import admin
from .models import Projeto, Roteiro, Cenario


class ProjetoAdmin(admin.ModelAdmin):
   list_display = ("nome", "descricao", "responsavel")

admin.site.register(Projeto, ProjetoAdmin)

class CenarioAdmin(admin.ModelAdmin):
   list_display1 = ("nome", "descricao", "data_criacao")

admin.site.register(Cenario, CenarioAdmin)

class RoteiroAdmin(admin.ModelAdmin):
   list_display2 = ("nome", "descricao", "projetos", "cenarios")

admin.site.register(Roteiro, RoteiroAdmin)