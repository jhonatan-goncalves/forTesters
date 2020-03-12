from django.urls import path
from . import views

urlpatterns = [
    path('', views.projeto_lista, name='projeto_lista'),
]