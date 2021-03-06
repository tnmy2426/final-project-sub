from django.urls import path
from . import views

app_name = 'App_Event'

urlpatterns = [
    path('', views.EventList, name='event_list'),
    path('free-events', views.FreeEventList, name='free_event_list'),
    path('event-details/<pk>/', views.EventDetails, name='event_details'),
    path('add-event-notice/<pk>/', views.AddEventNotice, name='add_event_notice'),
    path('delete-event-notice/<pk>/', views.DeleteEventNotice, name='delete_event_notice'),
    path('add-event-photo/<pk>/', views.AddEventPhoto, name='add_event_photo'),
    path('delete-event-photo/<pk>/', views.DeleteEventPhoto, name='delete_event_photo'),
    path('create-event/', views.CreateEvent, name='create_event'),
    path('event-registration/<pk>/', views.EventRegistration, name='event_registration_view'),
    path('confirm-registration/<str:token>/', views.ConfirmRegistration, name='confirm_registration'),
]
