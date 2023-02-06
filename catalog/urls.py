from django.urls import path
from catalog.views import *


urlpatterns = [
    path('category/add', MenuCategoryCreateView.as_view(), name='menu_category_create'),
    path('category/index', MenuCategoryListView.as_view(), name='menu_category_index'),
    path('category/<int:pk>/detail', MenuCategoryDetailView.as_view(), name='menu_category_detail'),
    path('category/<int:pk>/edit', MenuCategoryUpdateView.as_view(), name='menu_category_edit'),
    path('category/<int:pk>/delete', MenuCategoryDeleteView.as_view(), name='menu_category_delete'),


    path('class/add', MenuClassCreateView.as_view(), name='menu_class_create'),
    path('class/index', MenuClassListView.as_view(), name='menu_class_index'),
    path('class/<int:pk>/detail', MenuClassDetailView.as_view(), name='menu_class_detail'),
    path('class/<int:pk>/edit', MenuClassUpdateView.as_view(), name='menu_class_edit'),
    path('class/<int:pk>/delete', MenuClassDeleteView.as_view(), name='menu_class_delete'),


    path('menu/add', MenuCreateView.as_view(), name='menu_create'),
    path('menu/index', MenuListView.as_view(), name='menu_index'),
    path('menu/<int:pk>/detail', MenuDetailView.as_view(), name='menu_detail'),
    path('menu/<int:pk>/edit', MenuUpdateView.as_view(), name='menu_edit'),
    path('menu/<int:pk>/delete', MenuDeleteView.as_view(), name='menu_delete'),

]

