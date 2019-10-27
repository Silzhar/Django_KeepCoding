from django.shortcuts import render
from django.contrib.auth import logout as django_logout

def login(request):
    return render(request, 'users/login.html')


def logout(request):
    if request.user.is_authenticaded():
        django_logout(request)
    return redirect('photos_home')