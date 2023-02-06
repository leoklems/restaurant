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
from admin_site.models import *
from admin_site.forms import *


class AdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'site_admin/dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class SiteInfoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = SiteInfoModel
    form_class = SiteInfoForm
    template_name = 'site_admin/info/create.html'
    success_message = 'Site Info Saved successfully'

    def dispatch(self, *args, **kwargs):
        try:
            site_info = SiteInfoModel.objects.get(pk=1)
        except SiteInfoModel.DoesNotExist:
            return super(SiteInfoCreateView, self).dispatch(*args, **kwargs)
        return redirect(reverse('admin_dashboard'))

    def get_success_url(self):
        return reverse('site_info_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SiteInfoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = SiteInfoModel
    form_class = SiteInfoForm
    template_name = 'site_admin/info/update.html'
    success_message = 'Organization Info Saved successfully'

    def get_success_url(self):
        return reverse('site_info_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SiteInfoDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    model = SiteInfoModel
    template_name = 'site_admin/info/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
