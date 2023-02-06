from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),
    path('django-admin/', admin.site.urls),
    path('accounts/', include('account.urls')),
    path('admin/', include('admin_site.urls')),
    path('admin/catalog/', include('catalog.urls')),
    path('reservation/', include('reservation.urls')),
    path('order/', include('order.urls')),
    path('gallery/', include('gallery.urls')),
    path('books/', include('book.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
