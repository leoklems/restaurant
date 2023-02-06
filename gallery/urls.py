from django.urls import path
from gallery.views import *


urlpatterns = [

    path('gallery/add', GalleryCreateView.as_view(), name='gallery_create'),
    path('gallery/index', GalleryListView.as_view(), name='gallery_index'),
    path('gallery/<int:pk>/detail', GalleryDetailView.as_view(), name='gallery_detail'),
    path('gallery/<int:pk>/edit', GalleryUpdateView.as_view(), name='gallery_edit'),
    path('gallery/<int:pk>/delete', GalleryDeleteView.as_view(), name='gallery_delete'),

]

