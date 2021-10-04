from django.urls import path
from . import views

app_name = 'App_Volunteer'

urlpatterns = [
    path('add-volunteer/<pk>/', views.AddVolunteer, name='add_volunteer'),
    path('volunteer-profile/', views.VolunteerProfile, name='volunteer_profile'),
]
