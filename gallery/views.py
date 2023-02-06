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
from gallery.models import *
from gallery.forms import *


class GalleryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = GalleryModel
    form_class = GalleryForm
    template_name = 'gallery/image/create.html'
    success_message = 'Image Added Successfully'

    def get_success_url(self):
        return reverse('gallery_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GalleryListView(LoginRequiredMixin, ListView):
    model = GalleryModel
    fields = '__all__'
    template_name = 'gallery/image/index.html'
    context_object_name = "gallery_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GalleryDetailView(LoginRequiredMixin, DetailView):
    model = GalleryModel
    fields = '__all__'
    template_name = 'gallery/image/detail.html'
    context_object_name = "gallery"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GalleryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = GalleryModel
    form_class = GalleryForm
    template_name = 'gallery/image/edit.html'
    success_message = 'Image Successfully Updated'

    def get_success_url(self):
        return reverse('gallery_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GalleryDeleteView(LoginRequiredMixin, DeleteView):
    model = GalleryModel
    fields = '__all__'
    template_name = 'gallery/image/delete.html'
    success_message = 'Gallery Successfully Deleted'
    context_object_name = "gallery"

    def get_success_url(self):
        return reverse('gallery_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
