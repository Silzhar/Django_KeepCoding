# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from photos.models import Photo

def home(request):
    photos = Photo.objects.all()
    return render(request, 'photos/home.html')



    '''
    html = '<ul>'
    for photo in photos:
        html += '<li>' + photo.name + '</li>'
    html += '</ul>'
    return HttpResponse(html)   '''