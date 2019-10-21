# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from photos.models import Photo, PUBLIC

def home(request):
    photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at') # query :for last photos created
    context = {
        'photos_list': photos[:4] # only 4 photos in home page
    }
    return render(request, 'photos/home.html', context)

def detail(request, pk):
    '''
    Carga la página de detalle de una foto
    param request: HttpRequest
    param pk: id de la foto
    return: HttpResponse
    '''
    '''
    # sintaxtis de recuperación de un objeto
    # lo mismo que abajo pero controlando con Try / except
    try:  
        photo = Photo.objects.get(pk=pk)
    except Photo.DoesNotExist:
        photo = None
    except Photo.MultipleObjects:
        photo = None
    '''

    possible_photos = Photo.objects.filter(pk=pk) # pk = primary key
    photo = possible_photos[0] if len(possible_photos) >= 1 else None
    if photo is not None:
        # cargar la plantilla de detalle
        context = {
            'photo': photo
        }
        return render(request, 'photos/detail.html', context)
    else:
        return HttpResponseNotFound('No existe la foto') # 404 not found
