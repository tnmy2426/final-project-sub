
from django.shortcuts import render, redirect, get_object_or_404

from .models import Event, EventNotice, EventPhoto
from .forms import EventForm, EventRegistrationForm, EventNoticeForm
from App_Participant.models import Participant

# Decorators
from django.contrib.auth.decorators import login_required
from App_ClubAdmin.decorators import group_required

#For messages
from django.contrib import messages

# Create your views here.

def EventList(request):
    events = Event.objects.all()
    return render(request, "App_Event/event_list.html", {"events":events})

def EventDetails(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event_notices = EventNotice.objects.filter(event=event)
    return render(request, "App_Event/event_details.html", {"event":event, "event_notices": event_notices})

def EventRegistration(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = EventRegistrationForm()
    if request.method == "POST":
        form = EventRegistrationForm(request.POST or None)
        if form.is_valid():
            participant = form.save(commit=False)
            participant.event_id = event.id
            event_reg_id = participant.event_reg_id
            if not Participant.objects.filter(event_reg_id=event_reg_id, event=event).exists():
                Participant.objects.create(
                    event_reg_id=event_reg_id, event=event, participant_name= participant.participant_name, 
                    participant_email=participant.participant_email, phone_no=participant.phone_no, guests=participant.guests,
                    fee_amount=participant.fee_amount, payment_status=participant.payment_status, transaction_id=participant.transaction_id
                )
                messages.success(request, f"Registration Successful in {event.event_title}. ")
                return redirect("App_Event:event_details", pk=event.id)
            else:
                form = EventRegistrationForm()
                error_message = f"{event_reg_id} ID already taken!!!"
                return render(request, "App_Event/event_registration.html", {"form":form, "error_message":error_message})
    return render(request, "App_Event/event_registration.html", {"form":form})


@login_required
@group_required("ClubAdmin")
def CreateEvent(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event_obj = form.save(commit=False)
            event_obj.user = request.user
            event_obj.save()
            messages.success(request, "Event Created Successfully!!")
            return redirect ("App_Event:event_list")
    return render(request, "App_Event/create_event.html", {"form":form} )

@login_required
@group_required("ClubAdmin")
def AddEventNotice(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = EventNoticeForm()
    if request.method == "POST":
        form = EventNoticeForm(request.POST or None)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.event_id = event.id
            notice.save()
            messages.success(request, f"{event.event_title}'s Notice updated!!")
            return redirect("App_Event:event_details", pk=event.id)
        else:
            form = EventNoticeForm()
    return render(request, "App_Event/event_notice.html", {"form": form})

@login_required
@group_required("ClubAdmin")
def DeleteEventNotice(request, pk):
    notice = EventNotice.objects.get(id=pk)
    notice.delete()
    messages.warning(request, "Notice Deleted!!")
    return redirect("App_Event:event_list")



