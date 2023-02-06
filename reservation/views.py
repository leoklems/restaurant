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
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.db.models import Q, Sum
from datetime import date, datetime, timedelta
from django.shortcuts import get_object_or_404
from reservation.models import *
from reservation.forms import *


class PreferenceCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = PreferenceModel
    form_class = PreferenceForm
    template_name = 'reservation/preference/create.html'
    success_message = 'Preference Added Successfully'

    def get_success_url(self):
        return reverse('preference_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PreferenceListView(LoginRequiredMixin, ListView):
    model = PreferenceModel
    fields = '__all__'
    template_name = 'reservation/preference/index.html'
    context_object_name = "preference_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PreferenceDetailView(LoginRequiredMixin, DetailView):
    model = PreferenceModel
    fields = '__all__'
    template_name = 'reservation/preference/detail.html'
    context_object_name = "preference"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PreferenceUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = PreferenceModel
    form_class = PreferenceForm
    template_name = 'reservation/preference/edit.html'
    success_message = 'Preference Successfully Updated'

    def get_success_url(self):
        return reverse('preference_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PreferenceDeleteView(LoginRequiredMixin, DeleteView):
    model = PreferenceModel
    fields = '__all__'
    template_name = 'reservation/preference/delete.html'
    success_message = 'Preference Successfully Deleted'
    context_object_name = "preference"

    def get_success_url(self):
        return reverse('preference_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
        
        
class TableCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = TableModel
    form_class = TableForm
    template_name = 'reservation/table/create.html'
    success_message = 'Table Added Successfully'

    def get_success_url(self):
        return reverse('table_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TableListView(LoginRequiredMixin, ListView):
    model = TableModel
    fields = '__all__'
    template_name = 'reservation/table/index.html'
    context_object_name = "table_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TableDetailView(LoginRequiredMixin, DetailView):
    model = TableModel
    fields = '__all__'
    template_name = 'reservation/table/detail.html'
    context_object_name = "table"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TableUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = TableModel
    form_class = TableForm
    template_name = 'reservation/table/edit.html'
    success_message = 'Table Successfully Updated'

    def get_success_url(self):
        return reverse('table_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TableDeleteView(LoginRequiredMixin, DeleteView):
    model = TableModel
    fields = '__all__'
    template_name = 'reservation/table/delete.html'
    success_message = 'Table Successfully Deleted'
    context_object_name = "table"

    def get_success_url(self):
        return reverse('table_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
        
        
class ReservationCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ReservationModel
    form_class = ReservationForm
    template_name = 'reservation/reservation/create.html'
    success_message = 'Reservation Made Successfully'

    def get_success_url(self):
        return reverse('reservation_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ReservationListView(LoginRequiredMixin, ListView):
    model = ReservationModel
    fields = '__all__'
    template_name = 'reservation/reservation/index.html'
    context_object_name = "reservation_list"
    
    def get_queryset(self, **kwargs):
        return ReservationModel.objects.all().order_by('created_at').reverse()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ReservationDetailView(LoginRequiredMixin, DetailView):
    model = ReservationModel
    fields = '__all__'
    template_name = 'reservation/reservation/detail.html'
    context_object_name = "reservation"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ReservationUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ReservationModel
    form_class = ReservationForm
    template_name = 'reservation/reservation/edit.html'
    success_message = 'Reservation Successfully Updated'

    def get_success_url(self):
        return reverse('reservation_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ReservationDeleteView(LoginRequiredMixin, DeleteView):
    model = ReservationModel
    fields = '__all__'
    template_name = 'reservation/reservation/delete.html'
    success_message = 'Reservation Successfully Deleted'
    context_object_name = "reservation"

    def get_success_url(self):
        return reverse('reservation_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
        
 
@csrf_exempt
@require_http_methods(["POST"])
def make_reservation(request):
    form = ReservationForm(request.POST)
    if form.is_valid():
        reservation = form.save(commit=False)
        reservation.confirmation_status = 'pending'
        reservation.mode = 'online'
        reservation.save()
        if reservation.id:
            reservation = ReservationModel.objects.get(pk=reservation.id)
            message = "Your booking request was successful. We will call back or send an Email to confirm your reservation. Thank you!. ID: {}".format(reservation.code)
            return HttpResponse(message)
        return HttpResponse("Error making Reservation. Please Check inputed data and try again")
    
    return HttpResponse("Error making Reservation. Please Check inputed data and try again")
    
