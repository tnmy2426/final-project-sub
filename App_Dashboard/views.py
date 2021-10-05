from django.shortcuts import get_object_or_404, render

# Models
from App_ClubAdmin.models import ClubAdmin
from App_Event.models import Event, EventVolunteer, EventNotice, EventPhoto
from App_Participant.models import Participant, ParticipantStatus
from App_Volunteer.models import Volunteer
from django.contrib.auth import get_user_model

# Decoratores
from django.contrib.auth.decorators import login_required
from App_ClubAdmin.decorators import group_required

User = get_user_model()
# Create your views here.

@login_required
@group_required("ClubAdmin")
def ActiveEventList(request):
    events = Event.objects.all()
    print(events)
    return render(request, "App_Dashboard/active_event_list.html", {"events":events})

@login_required
def ActiveEventDetails(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, "App_Dashboard/active_event_details.html", {"event":event})
