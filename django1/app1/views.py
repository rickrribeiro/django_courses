from django.shortcuts import render
from .models import Produto
# Create your views here.

def index(request):
    print(dir(request.user))
    if str(request.user) == 'AnonymousUser':
        teste = 'Usuário não logado'
    else:
        teste = 'Usuario logado'

    produtos = Produto.objects.all()
    context ={
        'curso':'Programação django',
        'outro':'outro param',
        'logado' : teste,
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, id):
    prod = Produto.objects.get(id=id)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)