#For messages
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

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
    active_events = Event.objects.filter(is_active=True)
    inactive_events = Event.objects.filter(is_active=False)
    context = {"active_events":active_events, "inactive_events":inactive_events}
    return render(request, "App_Dashboard/active_event_list.html", context)

@login_required
@group_required("ClubAdmin")
def DeactivateEvent(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if event.is_active == True:
        event.is_active = False
        event.save()
        event_volunteers = EventVolunteer.objects.filter(event=event)
        print(event_volunteers)
        for event_volunteer in event_volunteers:
            user = User.objects.get(username=event_volunteer, is_volunteer=True)
            print(user)
            user.delete()
        messages.warning(request, f"{event.event_title} Deactivated !!!")
        return redirect("App_Dashboard:active_event")
    return render(request, "App_Dashboard/active_event_list.html", {})

@login_required
def ActiveEventDetails(request, pk):
    event = get_object_or_404(Event, pk=pk)
    verified_participants = ParticipantStatus.objects.filter(event=event, payment_status=True )
    context = {"event":event, "verified_participants":verified_participants}
    return render(request, "App_Dashboard/active_event_details.html", context)

@login_required
def EventParticipantList(request, pk):
    event = get_object_or_404(Event, pk=pk)
    participants = Participant.objects.filter(event=event, payment_status=False)
    return render(request, "App_Dashboard/event_participant_list.html", {"participants":participants, "event":event})

@login_required
def VerifyParticipant(request, pk):
    participant = Participant.objects.get(id=pk)
    if participant.payment_status == False:
        participant.payment_status = True
        participant.participant_status.payment_status = True
        participant.save()
        status = ParticipantStatus.objects.get(event=participant.event, participant=participant)
        status.payment_status = True
        status.save()
        messages.success(request, f"{participant.event_reg_id} registration verified !!!")
    return redirect("App_Dashboard:event_participants", pk=participant.event_id)


@login_required
def Attendence(request, pk):
    participant = Participant.objects.get(id=pk)
    status = ParticipantStatus.objects.get(event = participant.event, participant=participant)
    if status.attendence == False:
        status.attendence = True
        status.save()
        messages.success(request, f"{status.participant.participant_name} Attended !!!")
    return redirect("App_Dashboard:active_event_details", pk=status.event.id)
 

@login_required
def KitToken(request, pk):
    participant = Participant.objects.get(id=pk)
    status = ParticipantStatus.objects.get(event = participant.event, participant=participant)
    if status.kit_token == False:
        status.kit_token = True
        status.save()
        messages.success(request, f"{status.participant.event_reg_id} Kit received !!!")
    return redirect("App_Dashboard:active_event_details", pk=status.event.id)

@login_required
def BreakfastToken(request, pk):
    participant = Participant.objects.get(id=pk)
    status = ParticipantStatus.objects.get(event = participant.event, participant=participant)
    if status.breakfast_token == False:
        status.breakfast_token = True
        status.save()
        messages.success(request, f"{status.participant.event_reg_id} Breakfat received !!!")
    return redirect("App_Dashboard:active_event_details", pk=status.event.id)

@login_required
def LunchToken(request, pk):
    participant = Participant.objects.get(id=pk)
    status = ParticipantStatus.objects.get(event = participant.event, participant=participant)
    if status.lunch_token == False:
        status.lunch_token = True
        status.save()
        messages.success(request, f"{status.participant.event_reg_id} Lunch received !!!")
    return redirect("App_Dashboard:active_event_details", pk=status.event.id)
    

@login_required
def SnacksToken(request, pk):
    participant = Participant.objects.get(id=pk)
    status = ParticipantStatus.objects.get(event = participant.event, participant=participant)
    if status.snacks_token == False:
        status.snacks_token = True
        status.save()
        messages.success(request, f"{status.participant.event_reg_id} Snacks received !!!")
    return redirect("App_Dashboard:active_event_details", pk=status.event.id)

@login_required
def MiscToken(request, pk):
    participant = Participant.objects.get(id=pk)
    status = ParticipantStatus.objects.get(event = participant.event, participant=participant)
    if status.misc_token == False:
        status.misc_token = True
        status.save()
        messages.success(request, f"{status.participant.event_reg_id} Misc received !!!")
    return redirect("App_Dashboard:active_event_details", pk=status.event.id)


#-----------Dashboard for Volunteer---------------#

@login_required
@group_required("Volunteer")
def VolunteerDashboard(request):
    user = request.user
    volunteer = Volunteer.objects.get(user=user)
    event_volunteer = EventVolunteer.objects.get(volunteer=volunteer)
    event = get_object_or_404(Event, id=event_volunteer.event.id)
    return render (request, "App_Dashboard/volunteer_dashboard.html", {"event":event})