from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Services
from .services import comparePasswords


def index(request):
    return render(request, 'public/index.html')


def loginRoute(request):
    context = {
        'register_form': UserCreationForm,
        'login_form': AuthenticationForm,
        'error': ""
    }
    if request.method == 'GET':
        return render(request, 'public/login.html', context)
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        email = request.POST['email']
        if comparePasswords(pass1, pass2):
            try:
                user = User.objects.create_user(
                    email=email,
                    username=username, password=pass1)
                user.save()
                login(request, user)
                return redirect('/polls/')
            except IntegrityError:
                context['error'] = "Error al crear el usuario"
                return render(request, 'public/login.html', context)
        else:
            context['error'] = "Las contraseñas no coinciden"
            return render(request, 'public/login.html', context)


def signout(request):
    logout(request)
    return redirect('')


def signin(request):
    context = {
        'form': AuthenticationForm,
        'error': ""
    }
    if request.method == 'GET':
        return render(request, 'public/login.html', context)
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            context['error_login'] = "Datos invalidos"
            return render(request, 'public/login.html', context)
        else:
            login(request, user)
            return redirect('/polls/')
