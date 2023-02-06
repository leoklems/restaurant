from django.urls import path
from admin_site.views import *


urlpatterns = [
    path('', AdminDashboardView.as_view(), name='admin_dashboard'),
    
    path('info/create', SiteInfoCreateView.as_view(), name='site_info_create'),
    path('info/detail/<int:pk>', SiteInfoDetailView.as_view(), name='site_info_detail'),
    path('info/update/<int:pk>', SiteInfoUpdateView.as_view(), name='site_info_update'),

    
]

