from django.views.generic.detail import DetailView
from django.http import JsonResponse

from . import models
from . import services

class GalleryView(DetailView):
    model = models.Gallery

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        files = services.get_files_from_folder(self.object.user_id)
        context["files"] = files
        return context
    
def gallery_api(request, pk):
    gallery = models.Gallery.objects.get(pk=pk)
    return JsonResponse(gallery.data)