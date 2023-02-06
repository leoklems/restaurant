from django.urls import path
from order.views import *


urlpatterns = [
    
    path('make', make_cart_view, name='make_cart'),

]

