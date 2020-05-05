from django.urls import path
from . import views

urlpatterns = [
    path('', views.projeto_lista, name='projeto_lista'),
    path('', views.roteiro_lista, name='roteiro_lista'),
    path('', views.cenario_lista, name='cenario_lista'),
]