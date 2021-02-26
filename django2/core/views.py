from django.shortcuts import render
from .forms import ContatoForm, ProdutoModelForm
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contato(request):
    form = ContatoForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail!')

    context = {
        'form' : form
    }
    return render(request, 'contato.html', context)

def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)
            print(f'Nome: {prod.nome}')
            print(f'Preco: {prod.preco}')
            print(f'est: {prod.estoque}')
            print(f'IMG: {prod.imagem}')
            messages.success(request, 'Produto salvo com sucesso.')
            form = ProdutoModelForm()
        else:
            messages.error(request, 'Erro ao salvar produto')
    else:
        form = ProdutoModelForm()
    context ={
        'form': form
    }
    return render(request, 'produto.html', context)