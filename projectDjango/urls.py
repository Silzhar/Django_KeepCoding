"""projectDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from photos.views import HomeView, DetailView
from users.views import LoginView, LogoutView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Photos URLs
    url(r'^$', HomeView.as_view(), name='photos_home'), 
    url(r'^photos/(?P<pk>[0-9]+)$', DetailView.as_view(), name='photo_detail'), # (?P<pk>[0-9]+) = cualquier numero de 0 a 9 repetido una o mas veces
    url(r'^photos/new$', 'photos.views.create', name='create_photo'),

    # Users URLs
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout')
]
