from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import Projeto
from .querysets import getProjectsByLanguage
# Create your views here.

def index(request):
    # print(dir(request.user))

    # if str(request.user) == 'AnonymousUser':
    #     teste = 'Usuário não logado'
    # else:
    #     teste = 'Usuario logado'

    projetosNode = getProjectsByLanguage('Node')
    #projetosPython = getProjectsByLanguage('Python')
    projetosPython ='erro aq' # Projeto.objects.filter(linguagem='Python')
    projetosReact = getProjectsByLanguage('React')
    projetosHTML = getProjectsByLanguage('HTML')
    context ={
       'projetosNode': projetosNode,
       'projetosPython':projetosPython,
       'projetosReact':projetosReact,
       'projetosHTML':projetosHTML
    
    }
    print(projetosPython)
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, id):
    #prod = Produto.objects.get(id=id)
    prod = get_object_or_404(Produto, id=id)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type = 'text/html;charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type = 'text/html;charset=utf8', status=404)