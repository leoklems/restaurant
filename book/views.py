from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.template import RequestContext
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Q, Sum
from datetime import date, datetime, timedelta
from django.shortcuts import get_object_or_404
from book.models import *
from book.forms import *


class BookCategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = BookCategoryModel
    form_class = BookCategoryForm
    template_name = 'book/category/create.html'
    success_message = 'Category Added Successfully'

    def get_success_url(self):
        return reverse('book_category_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BookCategoryListView(LoginRequiredMixin, ListView):
    model = BookCategoryModel
    fields = '__all__'
    template_name = 'book/category/index.html'
    context_object_name = "book_category_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BookCategoryDetailView(LoginRequiredMixin, DetailView):
    model = BookCategoryModel
    fields = '__all__'
    template_name = 'book/category/detail.html'
    context_object_name = "book_category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BookCategoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = BookCategoryModel
    form_class = BookCategoryForm
    template_name = 'book/category/edit.html'
    success_message = 'Category Successfully Updated'

    def get_success_url(self):
        return reverse('book_category_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BookCategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = BookCategoryModel
    fields = '__all__'
    template_name = 'book/category/delete.html'
    success_message = 'Category Successfully Deleted'
    context_object_name = "book_category"

    def get_success_url(self):
        return reverse('book_category_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BookCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = BookModel
    form_class = BookForm
    template_name = 'book/book/create.html'
    success_message = 'Book Added Successfully'

    def get_success_url(self):
        return reverse('book_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BookListView(LoginRequiredMixin, ListView):
    model = BookModel
    fields = '__all__'
    template_name = 'book/book/index.html'
    context_object_name = "book_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BookDetailView(LoginRequiredMixin, DetailView):
    model = BookModel
    fields = '__all__'
    template_name = 'book/book/detail.html'
    context_object_name = "book"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BookUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = BookModel
    form_class = BookForm
    template_name = 'book/book/edit.html'
    success_message = 'Book Successfully Updated'

    def get_success_url(self):
        return reverse('book_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = BookModel
    fields = '__all__'
    template_name = 'book/book/delete.html'
    success_message = 'Book Successfully Deleted'
    context_object_name = "book"

    def get_success_url(self):
        return reverse('book_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
