from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('login.html/', views.Login.as_view(), name='login'),
    ###-------------------------Cenários-------------------------
    path('cenario_lista.html/', views.cenario_lista, name='cenario_lista'),
    path('cenario/<int:pk>/', views.cenario_detalhes, name='cenario_detalhes'),
    path('cenario/novo/', views.cenario_novo, name='cenario_novo'),
    path('cenario/<int:pk>/edicao/', views.cenario_edicao, name='cenario_edicao'),
    path('cenario/<int:pk>', views.cenario_deletar, name='cenario_deletar'),
    ###-------------------------Roteiros-------------------------
    path('roteiro_lista.html/', views.roteiro_lista, name='roteiro_lista'),
    path('roteiro/<int:pk>/', views.roteiro_detalhes, name='roteiro_detalhes'),
    path('roteiro/novo/', views.roteiro_novo, name='roteiro_novo'),
    path('roteiro/<int:pk>/edicao/', views.roteiro_edicao, name='roteiro_edicao'),
    path('roteiro/<int:pk>', views.roteiro_deletar, name='roteiro_deletar'),
    ###-------------------------Projetos-------------------------
    path('projeto_lista.html/', views.projeto_lista, name='projeto_lista'),
    path('projeto/<int:pk>/', views.projeto_detalhes, name='projeto_detalhes'),
    path('projeto/novo/', views.projeto_novo, name='projeto_novo'),
    path('projeto/<int:pk>/edicao/', views.projeto_edicao, name='projeto_edicao'),
    path('projeto/<int:pk>', views.projeto_deletar, name='projeto_deletar'),
]
