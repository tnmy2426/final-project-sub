from django.shortcuts import render, redirect, get_object_or_404
from App_Event.models import Event, EventVolunteer
from App_Volunteer.models import Volunteer
from .forms import CreateVolunteer
from django.contrib.auth.decorators import login_required

# For Messages
from django.contrib import messages

# Create your views here.

def AddVolunteer(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = CreateVolunteer()
    if request.method == "POST":
        form = CreateVolunteer(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password("1234")
            user.is_active = True
            user.is_staff = True
            user.save()
            volunteer_profile = Volunteer(user=user)
            volunteer_profile.save()
            event_volunteer = EventVolunteer(event=event, volunteer=volunteer_profile)
            event_volunteer.save()
            messages.success(request, 'Volunteer Added!!!')
            return redirect("App_Event:event_details", pk=event.id)
    return render(request, "App_Volunteer/add_volunteer.html", {"form":form})