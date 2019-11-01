# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import logout as django_logout, authenticate, login as django_login
from users.forms import LoginForm

def login(request):
    form = LoginForm()
    error_messages = []
    if request.method == 'POST':
        username = request.POST.get('usr') # .get evita comflicto con contraseña errónea
        password = request.POST.get('pwd')
        user = authenticate(username=username, password=password) # busca encriptado de usuario y contraseña
        if user is None:
            error_messages.append('Nombre de usuario o contraseña incorrectos')
        else:
            if user.is_active:
                django_login(request, user)
                return ('photos_home')
            else:
                error_messages.append('El usuario no está activo')
                
    context = {
        'errors': error_messages,
        'login_form': form
    }
    return render(request, 'users/login.html', context)


def logout(request):
    if request.user.is_authenticaded():
        django_logout(request)
    return ('photos_home')