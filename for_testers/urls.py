from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('', views.projeto_lista, name='projeto_lista'),
    path('', views.roteiro_lista, name='roteiro_lista'),
    path('', views.cenario_lista, name='cenario_lista'),
]