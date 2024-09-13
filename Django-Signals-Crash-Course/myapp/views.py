from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.views import View
from .forms import SignUpForm

class Dashboard(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'myapp/dashboard.html')

class Register(View):
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'myapp/index.html', {'form': form})
    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard')
        else:
            form = SignUpForm()
            return redirect('register')

class Logout(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('register')

class Delete(View):
    def post(self, request, pk, *args, **kwargs):
        user = User.objects.filter(pk=pk).first()

        if user is not None:
            user.delete()
            return redirect('register')
