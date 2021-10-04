from django.contrib import admin
from django.urls import path, include

# For static files
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('App_ClubAdmin.urls')),
    path('volunteer/', include('App_Volunteer.urls')),
    path('', include('App_Event.urls')),
    path('participant/', include('App_Participant.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)