from django.urls import path
from .views import index,contato, produto


urlpatterns=[
    path('',index, name='index'),
    path('contato',contato),
    path('produto/<int:id>', produto, name='produto') #não pode ter esaço depois do <int: para n dar erro
]