from django.views.generic import FormView
from .models import Servico, Funcionario, Feature
from .forms import ContatoForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _
from django.utils import translation

# Create your views here.


class IndexView(FormView):
    template_name = "index.html"
    form_class = ContatoForm
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        lang = translation.get_language()
        context["servicos"] = Servico.objects.order_by("?").all()  # random order
        context["funcionarios"] = Funcionario.objects.order_by("nome").all()
        features = Feature.objects.all()
        context["featuresesq"] = features[: len(features) // 2]
        context["featuresdir"] = features[len(features) // 2 :]
        # print(context["funcionarios"][0].imagem)
        context["lang"] = lang
        translation.activate(lang)
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, _("email enviado com sucessor"))
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _("erro ao enviar email"))
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
