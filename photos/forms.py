# -*- coding: utf-8 -*-
from django import forms


class PhotoForm(forms.ModelForm):
    # Formulario para modelo Photo
    class Meta:
        model = Photo
        exclude = []