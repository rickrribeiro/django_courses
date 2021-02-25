from django import forms


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=30, min_length=1)
    email = forms.EmailField(label='E-mail', max_length=50)
    assunto = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea(), min_length=10)
