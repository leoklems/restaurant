from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.core.exceptions import PermissionDenied
from django.conf import settings
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.template import RequestContext
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from catalog.models import *
from gallery.models import *
from book.models import *


class HomePageView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_list'] = MenuModel.objects.filter(status='active')[:4]
        return context


class MenuPageView(TemplateView):
    template_name = 'home/menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_list'] = MenuModel.objects.filter(status='active')[:16]
        return context


class AboutPageView(TemplateView):
    template_name = 'home/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ContactPageView(TemplateView):
    template_name = 'home/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class GalleryPageView(TemplateView):
    template_name = 'home/gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery_list'] = GalleryModel.objects.all()
        return context


class SpecialPageView(TemplateView):
    template_name = 'home/special.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class VIPCardPageView(TemplateView):
    template_name = 'home/vip_card.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class CartPageView(TemplateView):
    template_name = 'home/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_list'] = MenuModel.objects.filter(status='active')[:16]
        return context
        
        
class BookPageView(TemplateView):
    template_name = 'home/book.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = BookModel.objects.all()
        return context
