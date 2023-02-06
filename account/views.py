import hashlib
import json

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.template import RequestContext
import html
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.exceptions import PermissionDenied
from django.conf import settings
import requests
from django.core.exceptions import ValidationError
import hmac
from datetime import datetime, timedelta
from ipaddress import ip_address, ip_network
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, JsonResponse,Http404
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from account.forms import SignUpForm, LoginForm
from account.models import *


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = request.POST['email']

            user = User.objects.create_user(username, email, password)
            user.is_active = False
            user.save()

            # send email to user to confirm to activate their account
            message_sent = send_activation_mail(request, user, email)
            if not message_sent:
                # notify admin of the failure
                pass
            request.session['registration_done'] = True
            return redirect('register_done')
    else:
        form = SignUpForm()
    context = {
        'form': form
    }
    return render(request, 'account/register.html', context)


def signup_done_view(request):
    if 'registration_done' in request.session:
        del request.session['registration_done']
        return render(request, 'account/register_done.html', {'registration_done': True})
        
    if 'activation_done' in request.session:
        del request.session['activation_done']
        return render(request, 'account/register_done.html',  {'activation_done': True})    

    return redirect('home')


def activate_account_view(request, uidb64, token):
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
        return HttpResponse(user.is_active)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        
        request.session['activation_done'] = True
        return redirect('register_done')
    else:  
        raise PermissionDenied()  


def signin_view(request):
    if request.method == 'POST':

        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # try to log user by either username or password
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                try:
                    user = User.objects.get(email=username)
                except User.DoesNotExist:
                    user = None
            if not user:
                messages.error(request, 'Invalid Username or Email ')

            else:
                username = user.username
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        messages.success(request, 'Welcome Back {}'.format(user.username))
                        if 'remember_login' in request.POST:
                            request.session.set_expiry(0)
                            request.session.modified = True

                        nxt = request.GET.get("next", None)
                        if nxt:
                            return redirect(request.GET.get('next'))
                        return redirect(reverse('admin_dashboard'))
                    else:
                        messages.error(request, 'Account not Activated')
                else:
                    messages.error(request, 'Incorrect Password')
        else:
            messages.error(request, 'Invalid Credentials')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'account/login.html', context)


def sign_out_view(request):
    logout(request)
    return redirect(reverse('login'))


