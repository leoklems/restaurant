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
from catalog.models import *
from catalog.forms import *


class MenuCategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = MenuCategoryModel
    form_class = MenuCategoryForm
    template_name = 'catalog/category/create.html'
    success_message = 'Category Added Successfully'

    def get_success_url(self):
        return reverse('menu_category_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MenuCategoryListView(LoginRequiredMixin, ListView):
    model = MenuCategoryModel
    fields = '__all__'
    template_name = 'catalog/category/index.html'
    context_object_name = "menu_category_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MenuCategoryDetailView(LoginRequiredMixin, DetailView):
    model = MenuCategoryModel
    fields = '__all__'
    template_name = 'catalog/category/detail.html'
    context_object_name = "menu_category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MenuCategoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = MenuCategoryModel
    form_class = MenuCategoryForm
    template_name = 'catalog/category/edit.html'
    success_message = 'Category Successfully Updated'

    def get_success_url(self):
        return reverse('menu_category_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MenuCategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = MenuCategoryModel
    fields = '__all__'
    template_name = 'catalog/category/delete.html'
    success_message = 'Category Successfully Deleted'
    context_object_name = "menu_category"

    def get_success_url(self):
        return reverse('menu_category_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MenuClassCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = MenuClassModel
    form_class = MenuClassForm
    template_name = 'catalog/class/create.html'
    success_message = 'Class Added Successfully'

    def get_success_url(self):
        return reverse('menu_class_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MenuClassListView(LoginRequiredMixin, ListView):
    model = MenuClassModel
    fields = '__all__'
    template_name = 'catalog/class/index.html'
    context_object_name = "menu_class_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MenuClassDetailView(LoginRequiredMixin, DetailView):
    model = MenuClassModel
    fields = '__all__'
    template_name = 'catalog/class/detail.html'
    context_object_name = "menu_class"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MenuClassUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = MenuClassModel
    form_class = MenuClassForm
    template_name = 'catalog/class/edit.html'
    success_message = 'Class Successfully Updated'

    def get_success_url(self):
        return reverse('menu_class_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MenuClassDeleteView(LoginRequiredMixin, DeleteView):
    model = MenuClassModel
    fields = '__all__'
    template_name = 'catalog/class/delete.html'
    success_message = 'Class Successfully Deleted'
    context_object_name = "menu_class"

    def get_success_url(self):
        return reverse('menu_class_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MenuCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = MenuModel
    form_class = MenuForm
    template_name = 'catalog/menu/create.html'
    success_message = 'Menu Added Successfully'

    def get_success_url(self):
        return reverse('menu_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MenuListView(LoginRequiredMixin, ListView):
    model = MenuModel
    fields = '__all__'
    template_name = 'catalog/menu/index.html'
    context_object_name = "menu_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MenuDetailView(LoginRequiredMixin, DetailView):
    model = MenuModel
    fields = '__all__'
    template_name = 'catalog/menu/detail.html'
    context_object_name = "menu"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MenuUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = MenuModel
    form_class = MenuForm
    template_name = 'catalog/menu/edit.html'
    success_message = 'Menu Successfully Updated'

    def get_success_url(self):
        return reverse('menu_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MenuDeleteView(LoginRequiredMixin, DeleteView):
    model = MenuModel
    fields = '__all__'
    template_name = 'catalog/menu/delete.html'
    success_message = 'Menu Successfully Deleted'
    context_object_name = "menu"

    def get_success_url(self):
        return reverse('menu_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
