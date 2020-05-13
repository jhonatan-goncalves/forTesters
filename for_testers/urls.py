from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('login.html/', views.Login.as_view(), name='login'),
    path('projeto_lista.html/', views.projeto_lista, name='projeto_lista'),
    path('roteiro_lista.html/', views.roteiro_lista, name='roteiro_lista'),
    path('cenario_lista.html/', views.cenario_lista, name='cenario_lista'),
]