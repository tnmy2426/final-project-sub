from App_Event import views
from django.urls import path
from . import views

app_name = 'App_Dashboard'

urlpatterns = [
    path('active-events/', views.ActiveEventList, name='active_event'),
    # path('login/', views.LoginView, name='login_view'),
    # path('logout/', views.LogoutView, name='logout_view'),
    # path('club-admin-profile/', views.ClubAdminProfile, name='club_admin_profile'),
    # path('club-admin-add-profile-pic/', views.AddProfilePic, name='add_profile_pic'),
]
