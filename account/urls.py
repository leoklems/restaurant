from django.urls import path
from account.views import *

urlpatterns = [
    path('register', signup_view, name='signup'),
    path('register/complete', signup_done_view, name='register_done'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', activate_account_view, name='activate_account'),
    path('login/', signin_view, name='login'),
    path('logout/', sign_out_view, name='logout'),

]

