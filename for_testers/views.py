from django.shortcuts import render

# Create your views here.
def projeto_lista(request):
    return render(request, 'for_testers/projeto_lista.html',{})