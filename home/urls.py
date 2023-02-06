from django.urls import path
from home.views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('menu', MenuPageView.as_view(), name='menu'),
    path('about', AboutPageView.as_view(), name='about'),
    path('contact', ContactPageView.as_view(), name='contact'),
    path('gallery', GalleryPageView.as_view(), name='gallery'),
    path('special', SpecialPageView.as_view(), name='special'),
    path('vip-cards', VIPCardPageView.as_view(), name='vip_cards'),
    path('cart', CartPageView.as_view(), name='cart'),
    path('books', BookPageView.as_view(), name='books'),
]

