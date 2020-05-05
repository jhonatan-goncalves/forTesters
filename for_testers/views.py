from django.shortcuts import render

# Create your views here.
def projeto_lista(request):
    return render(request, 'for_testers/projeto_lista.html',{})

def roteiro_lista(request):
    return render(request, 'for_testers/roteiro_lista.html',{})

def cenario_lista(request):
    return render(request, 'for_testers/cenario_lista.html',{})