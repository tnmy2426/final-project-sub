from django.urls import path
from . import views

app_name = 'App_Volunteer'

urlpatterns = [
    path('volunteers/', views.VolunteerList, name='volunteer_list'),
    path('add-volunteer/<pk>/', views.AddVolunteer, name='add_volunteer'),
    path('delete-volunteer/<pk>/', views.DeleteVolunteer, name='delete_volunteer'),
    path('volunteer-profile/', views.VolunteerProfile, name='volunteer_profile'),
    path('volunteer-password-change/', views.pass_change, name='volunteer_pass_change'),
]
