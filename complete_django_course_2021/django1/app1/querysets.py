from .models import Projeto
from django.db.models.query import QuerySet
# class TesteQueryset(models.QuerySet):
#     def getProjectsByLanguage(self, language):
#         lista = self.filter(linguagem=language)
#         return lista

def getProjectsGroupedByLanguage():
  #  list = Projeto.objects.filter(linguagem=language)
    #list = Projeto.objects.all()
    #print(list)
    #query = Projeto.objects.all().query
   # query.group_by = ['linguagem']
    #list = QuerySet(query=query, model=Projeto)
    list = Projeto.objects.raw('SELECT * FROM app1_projeto ORDER BY linguagem')
    print(list)
    return list