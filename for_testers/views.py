from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .models import Projeto, Roteiro, Cenario
from .forms import CenarioForm


# Create your views here.
class Index(LoginRequiredMixin, View):
    template = 'index.html'
    LOGIN_URL = '/login/'

    def get(self, request):
        projetos = Projeto.objects.all()
        return render(request, self.template, {'projetos': projetos})


class Login(View):
    template = 'login.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, self.template, {'form': form})


def projeto_lista(request):
    projetos = Projeto.objects.filter(
        data_criacao__lte=timezone.now()).order_by('id')
    return render(request, 'projeto_lista.html', {'projetos': projetos})


def roteiro_lista(request):
    roteiros = Roteiro.objects.filter(
        data_criacao__lte=timezone.now()).order_by('id')
    return render(request, 'roteiro_lista.html', {'roteiros': roteiros})


def cenario_lista(request):
    cenarios = Cenario.objects.filter(
        data_criacao__lte=timezone.now()).order_by('id')
    return render(request, 'cenario_lista.html', {'cenarios': cenarios})


class Index(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template)


def cenario_detalhes(request, pk):
    cenarios = get_object_or_404(Cenario, pk=pk)
    return render(request, 'cenario_detalhes.html', {'cenarios': cenarios})


def cenario_novo(request):
    if request.method == "POST":
        form = CenarioForm(request.POST)
        if form.is_valid():
            cenarios = form.save(commit=False)
            cenarios.data_criacao = timezone.now()
            cenarios.save()
            return redirect('cenario_detalhes', pk=cenarios.pk)
    else:
        form = CenarioForm()
    return render(request, 'cenario_edicao.html', {'form': form})


def cenario_edicao(request, pk):
    cenarios = get_object_or_404(Cenario, pk=pk)
    if request.method == "POST":
        form = CenarioForm(request.POST, instance=cenarios)
        if form.is_valid():
            cenarios = form.save(commit=False)
            cenarios.data_criacao = timezone.now()
            cenarios.save()
            return redirect('cenario_detalhes', pk=cenarios.pk)
    else:
        form = CenarioForm(instance=cenarios)
        return render(request, 'cenario_edicao.html', {'form': form})
