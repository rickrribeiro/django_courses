from django.views.generic import TemplateView
from .models import Servico, Funcionario

# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["servicos"] = Servico.objects.order_by("?").all()  # random order
        context["funcionarios"] = Funcionario.objects.order_by("?").all()
        # print(context["funcionarios"][0].imagem)
        return context