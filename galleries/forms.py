from django import forms

from . import models

class GalleryCreateForm(forms.ModelForm):
    model = models.Gallery
    fields = ("user, folder")