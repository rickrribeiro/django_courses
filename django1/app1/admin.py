from django.contrib import admin

# Register your models here.

from .models import Produto, Cliente, Projeto

#Campos para mostrar na tabela do admin
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')
    
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'linguagem', 'descricao')

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Projeto, ProjetoAdmin)