
from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, EventNotice, EventPhoto
from .forms import EventForm, EventRegistrationForm
from App_Participant.models import Participant

# Decorators
from django.contrib.auth.decorators import login_required

#For messages
from django.contrib import messages

# Create your views here.

def EventList(request):
    events = Event.objects.all()
    return render(request, "App_Event/event_list.html", {"events":events})

def EventDetails(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, "App_Event/event_details.html", {"event":event})

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