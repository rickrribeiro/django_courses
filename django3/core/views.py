from django.views.generic import FormView
from .models import Servico, Funcionario, Feature
from .forms import ContatoForm
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.


class IndexView(FormView):
    template_name = "index.html"
    form_class = ContatoForm
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["servicos"] = Servico.objects.order_by("?").all()  # random order
        context["funcionarios"] = Funcionario.objects.order_by("nome").all()
        features = Feature.objects.all()
        context["featuresesq"] = features[: len(features) // 2]
        context["featuresdir"] = features[len(features) // 2 :]
        # print(context["funcionarios"][0].imagem)
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, "email enviado com sucessor")
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        form.send_mail()
        messages.error(self.request, "erro ao enviar email")
        return super(IndexView, self).form_valid(form, *args, **kwargs)
