from .models import Projeto

# class TesteQueryset(models.QuerySet):
#     def getProjectsByLanguage(self, language):
#         lista = self.filter(linguagem=language)
#         return lista

def getProjectsByLanguage(language):
    lista = Projeto.objects.filter(linguagem=language)
    return lista