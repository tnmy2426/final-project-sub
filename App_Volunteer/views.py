from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from App_ClubAdmin.models import User
from django.contrib.auth.models import Group
from App_Event.models import Event, EventVolunteer
from App_Volunteer.models import Volunteer
from .forms import CreateVolunteer, VolunteerProfileForm
from django.contrib.auth.forms import PasswordChangeForm

#Decorators
from django.contrib.auth.decorators import login_required
from App_ClubAdmin.decorators import group_required

# For Messages
from django.contrib import messages

# Create your views here.

User = get_user_model()

#~~~~~~~~~~~~~~Views for Volunteer users~~~~~~~~~~~~~~~~

def VolunteerList(request):
    volunteers = Volunteer.objects.all()
    return render(request, "App_Volunteer/volunteer_list.html", {"volunteers": volunteers})

def AddVolunteer(request, pk):
    event = get_object_or_404(Event, pk=pk)
    volunteers = Volunteer.objects.all()
    form = CreateVolunteer()
    if request.method == "POST":
        form = CreateVolunteer(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'volunteer'
            user.set_password("1234")
            user.is_active = True
            user.is_volunteer = True
            user.save()
            group = Group.objects.get(name='Volunteer')
            user.groups.add(group)
            volunteer_profile = Volunteer(user=user)
            volunteer_profile.save()
            event_volunteer = EventVolunteer(event=event, volunteer=volunteer_profile)
            event_volunteer.save()
            messages.success(request, 'Volunteer Added!!!')
            return redirect("App_Event:event_details", pk=event.id)
    return render(request, "App_Volunteer/add_volunteer.html", {"form":form, "volunteers":volunteers, "event":event})


@login_required
@group_required("Volunteer")
def VolunteerProfile(request):
    profile = Volunteer.objects.get(user=request.user)
    form = VolunteerProfileForm(instance=profile)
    if request.method=="POST":
        form = VolunteerProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, f"Profile information updated!!!")
            form = VolunteerProfileForm(instance=profile)
    return render(request, 'App_Volunteer/volunteer_profile.html', {"form":form})


@login_required
def pass_change(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            changed = True
            messages.success(request, "You have successfully changed your password!!")
            return redirect('App_ClubAdmin:login_view')
    return render(request, 'App_Volunteer/change_password.html', context={'form':form})

#~~~~~~~~~~~~~~~~~~~~~~~~~ Views for ClubAdmin users ~~~~~~~~~~~~~~~~~~~~~~~~

@login_required
@group_required("ClubAdmin")
def DeleteVolunteer(request, pk):
    event_volunteer = EventVolunteer.objects.get(id=pk)
    event_volunteer.delete()
    # event_volunteer.volunteer.delete()
    event_volunteer.volunteer.user.is_active = False
    messages.warning(request, f"{event_volunteer.volunteer.user.full_name} Volunteer removed!!")
    return redirect("App_Event:event_list")