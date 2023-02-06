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


@csrf_exempt
@require_http_methods(["POST"])   
def make_cart_view(request):
    product_id = request.POST.get('id', None)
    amount = request.POST.get('amount', None)

    if not product_id:
        return HttpResponse('fail')

    cart = request.session.get('cart', None)
    
    if not cart:
        request.session['cart'] = {}
    
    cart = request.session['cart']
    if product_id in cart:
        del cart[product_id]
        request.session['cart'] = cart
        return HttpResponse('removed')

    else:
        cart[product_id] = [product_id, amount]
        request.session['cart'] = cart
        return HttpResponse('added')
    