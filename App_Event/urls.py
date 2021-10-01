from django.urls import path
from . import views

app_name = 'App_Event'

urlpatterns = [
    path('', views.EventList, name='event_list'),
    path('event-details/<pk>/', views.EventDetails, name='event_details'),
    path('create-event/', views.CreateEvent, name='create_event'),
    path('event-registration/<pk>/', views.EventRegistration, name='event_registration_view'),
]
