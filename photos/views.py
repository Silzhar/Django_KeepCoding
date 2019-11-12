# -*- coding: utf-8 -*-
from django.http import HttpResponseNotFound
from django.shortcuts import render
from photos.models import Photo, PUBLIC
from photos.forms import PhotoForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import View


class HomeView(View): # vista basada en clase
    def get(self, request):
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

    possible_photos = Photo.objects.filter(pk=pk).select_related('owner') # pk = primary key
    photo = possible_photos[0] if len(possible_photos) > 0 else None
    if photo is not None:
        # cargar la plantilla de detalle
        context = {
            'photo': photo
        }
        return render(request, 'photos/detail.html', context)
    else:
        return HttpResponseNotFound('No existe la foto') # 404 not found

@login_required()
def create(request):
    '''
    Formulario para creacion de de foto (petición POST)
    param request: HttpRequest
    return: HttpResponse
    '''

    success_message = ''
    if request.method == 'GET':
        form = PhotoForm()
    else:
        photo_with_owner = Photo()
        photo_with_owner.owner = request.user # Asignar como propietario de la foto al user autenticado
        form = PhotoForm(request.POST, instance=photo_with_owner)
        if form.is_valid():
            new_photo = form.save() # Guarda el objeto y lo devuelve
            form = PhotoForm() # Al no pasar valores aparece el formulario vacio
            success_message = 'Guardado con éxito'
            success_message += '<a href="{0}">'.format(reverse('photo_detail',args=[new_photo.pk]))
            success_message += 'ver foto'
            success_message += '</a>'

    context = {
        'form': form ,
        'success_message': success_message
    }
    return render(request, 'photos/new_photo.html', context)