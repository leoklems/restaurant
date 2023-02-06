from django.urls import path
from book.views import *


urlpatterns = [
    path('category/add', BookCategoryCreateView.as_view(), name='book_category_create'),
    path('category/index', BookCategoryListView.as_view(), name='book_category_index'),
    path('category/<int:pk>/detail', BookCategoryDetailView.as_view(), name='book_category_detail'),
    path('category/<int:pk>/edit', BookCategoryUpdateView.as_view(), name='book_category_edit'),
    path('category/<int:pk>/delete', BookCategoryDeleteView.as_view(), name='book_category_delete'),


    path('add', BookCreateView.as_view(), name='book_create'),
    path('index', BookListView.as_view(), name='book_index'),
    path('<int:pk>/detail', BookDetailView.as_view(), name='book_detail'),
    path('<int:pk>/edit', BookUpdateView.as_view(), name='book_edit'),
    path('<int:pk>/delete', BookDeleteView.as_view(), name='book_delete'),

]

