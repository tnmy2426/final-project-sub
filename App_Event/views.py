
from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, EventNotice, EventPhoto
from .forms import EventForm

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

