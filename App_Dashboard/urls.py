from App_Event import views
from django.urls import path
from . import views

app_name = 'App_Dashboard'

urlpatterns = [
    path('active-events/', views.ActiveEventList, name='active_event'),
    path('deactivate-event/<pk>/', views.DeactivateEvent, name='deactivate_event'),
    path('active-event-details/<pk>/', views.ActiveEventDetails, name='active_event_details'),
    path('event-participants/<pk>/', views.EventParticipantList, name='event_participants'),
    path('participant-verified/<pk>/', views.VerifyParticipant, name='verify_participant'),
    path('participant-attendence/<pk>/', views.Attendence, name='attendence_participant'),
    path('participant-kit-token/<pk>/', views.KitToken, name='kit_token'),
    path('participant-brkfast-token/<pk>/', views.BreakfastToken, name='breakfast_token'),
    path('participant-lunch-token/<pk>/', views.LunchToken, name='lunch_token'),
    path('participant-snacks-token/<pk>/', views.SnacksToken, name='snacks_token'),
    path('participant-misc-token/<pk>/', views.MiscToken, name='misc_token'),
    path('volunteer-dashboard/', views.VolunteerDashboard, name='volunteer_dashboard'),
]
