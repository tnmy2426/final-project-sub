import hashlib
from django.shortcuts import render, redirect, get_object_or_404

from .models import Event, EventNotice, EventPhoto, EventVolunteer
from .forms import EventForm, EventRegistrationForm, EventNoticeForm, EventPhotoForm
from App_Participant.models import Participant, ParticipantStatus
from App_Volunteer.models import Volunteer

#For email sending
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

# Decorators
from django.contrib.auth.decorators import login_required
from App_ClubAdmin.decorators import group_required

#For messages
from django.contrib import messages

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Create your views here ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~Views for all users~~~~~~~~~~~~~~~~

def EventList(request):
    events = Event.objects.filter(is_active=True)
    return render(request, "App_Event/event_list.html", {"events":events})

def EventDetails(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event_notices = EventNotice.objects.filter(event=event)
    event_photos = EventPhoto.objects.filter(event=event)
    event_volunteers = EventVolunteer.objects.filter(event=event)
    for volunteer in event_volunteers:
        print(volunteer)
    context = {
        "event":event, "event_notices": event_notices, "event_photos":event_photos, "event_volunteers":event_volunteers
    }
    return render(request, "App_Event/event_details.html", context)

def EventRegistration(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = EventRegistrationForm()
    if request.method == "POST":
        form = EventRegistrationForm(request.POST or None)
        if form.is_valid():
            get_email = form.cleaned_data.get('participant_email')
            print(get_email)
            participant = form.save(commit=False)
            participant.event_id = event.id
            event_reg_id = participant.event_reg_id
            if not Participant.objects.filter(event_reg_id=event_reg_id, event=event).exists():
                participant.email_confirmed = False
                participant_encoded = f'{participant.event_reg_id}'.encode()
                token = hashlib.sha224(participant_encoded).hexdigest()
                participant.token = token
                participant.save()

                #sending Email
                current_site  = get_current_site(request)
                email = get_email
                mail_subject = 'Confirm your registration.'
                email_body = render_to_string(
                    'App_Event/verify_email.html',
                        {
                            'event': event,
                            'participant': participant,
                            'event_reg_id': event_reg_id,
                            'email': email,
                            'participant_name':participant.participant_name,
                            'domain': current_site.domain,
                            'token': participant.token
                        }
                )
                send_mail(
                    subject=mail_subject,
                    message= email_body,
                    from_email='abdullah.al.nahdi2426@gmail.com',
                    recipient_list=[email],
                    fail_silently=True
                )

                # messages.success(request, f"Registration Successful in {event.event_title}. ")
                return render(request, "App_Event/register_start.html", {})
            else:
                form = EventRegistrationForm()
                error_message = f"{event_reg_id} ID already taken!!!"
                return render(request, "App_Event/event_registration.html", {"form":form, "error_message":error_message})
    return render(request, "App_Event/event_registration.html", {"form":form})

def ConfirmRegistration(request, token):
    participant = get_object_or_404(Participant, token=token)
    if participant is not None:
        participant.email_confirmed = True
        participant.save()
        ParticipantStatus.objects.create(
                event=participant.event, participant=participant, attendence=False, payment_status=False,kit_token=False, 
                breakfast_token=False, lunch_token=False, snacks_token=False, misc_token=False
        )
        return render(request, "App_Event/register_end.html", {})
    

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Views for ClubAdmins ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@login_required
@group_required("ClubAdmin")
def CreateEvent(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event_obj = form.save(commit=False)
            event_obj.user = request.user
            event_obj.is_active = True
            event_obj.save()
            messages.success(request, "Event Created Successfully!!")
            return redirect ("App_Event:event_list")
    return render(request, "App_Event/create_event.html", {"form":form})

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


@login_required
@group_required("ClubAdmin")
def AddEventPhoto(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = EventPhotoForm()
    if request.method == "POST":
        form = EventPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.event_id = event.id
            photo.save()
            messages.success(request, f"{event.event_title}'s Photo Uploaded!!")
            return redirect("App_Event:event_details", pk=event.id)
        else:
            form = EventPhotoForm()
    return render(request, "App_Event/event_photo.html", {"form": form})

@login_required
@group_required("ClubAdmin")
def DeleteEventPhoto(request, pk):
    photo = EventPhoto.objects.get(id=pk)
    photo.delete()
    messages.warning(request, "Photo Removed!!")
    return redirect("App_Event:event_list")