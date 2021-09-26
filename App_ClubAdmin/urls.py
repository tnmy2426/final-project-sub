from App_Event import views
from django.urls import path
from . import views

app_name = 'App_ClubAdmin'

urlpatterns = [
    path('signup/', views.ClubAdminSignup, name='clubadmin_signup'),
    path('login/', views.LoginView, name='login_view'),
    path('logout/', views.LogoutView, name='logout_view'),
    # path('club-admin-profile/', views.ClubAdminProfile, name='club_admin_profile'),
]
