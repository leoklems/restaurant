from django.urls import path
from reservation.views import *


urlpatterns = [
    path('add', ReservationCreateView.as_view(), name='reservation_create'),
    path('index', ReservationListView.as_view(), name='reservation_index'),
    path('<int:pk>/detail', ReservationDetailView.as_view(), name='reservation_detail'),
    path('<int:pk>/edit', ReservationUpdateView.as_view(), name='reservation_edit'),
    path('<int:pk>/delete', ReservationDeleteView.as_view(), name='reservation_delete'),
    
    path('make', make_reservation, name='make_reservation'),


    path('table/add', TableCreateView.as_view(), name='table_create'),
    path('table/index', TableListView.as_view(), name='table_index'),
    path('table/<int:pk>/detail', TableDetailView.as_view(), name='table_detail'),
    path('table/<int:pk>/edit', TableUpdateView.as_view(), name='table_edit'),
    path('table/<int:pk>/delete', TableDeleteView.as_view(), name='table_delete'),
    
    
    path('preference/add', PreferenceCreateView.as_view(), name='preference_create'),
    path('preference/index', PreferenceListView.as_view(), name='preference_index'),
    path('preference/<int:pk>/detail', PreferenceDetailView.as_view(), name='preference_detail'),
    path('preference/<int:pk>/edit', PreferenceUpdateView.as_view(), name='preference_edit'),
    path('preference/<int:pk>/delete', PreferenceDeleteView.as_view(), name='preference_delete'),


]

