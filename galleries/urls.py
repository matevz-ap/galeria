from django.urls import path

from . import views

urlpatterns = [
    path('<pk>', views.GalleryView.as_view(), name='gallery'),
    path('<pk>/json', views.gallery_api, name='gallery_api'),
]