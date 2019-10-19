# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from photos.models import Photo

def home(request):
    photos = Photo.objects.all().order_by('-created_at') # query :for last photos created
    context = {
        'photos_list': photos[:4] # only 4 photos in home page
    }
    return render(request, 'photos/home.html', context)



    '''
    html = '<ul>'
    for photo in photos:
        html += '<li>' + photo.name + '</li>'
    html += '</ul>'
    return HttpResponse(html)   '''