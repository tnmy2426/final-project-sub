from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from .models import User, ClubAdmin
from .forms import CreateNewUser, LoginUser

# For Messages
from django.contrib import messages

# For Authentication
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def ClubAdminSignup(request):
    form = CreateNewUser()
    if request.method == "POST":
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            messages.success(request, 'Registration Successfull. Your profile will be verified by an Admin!')
            return HttpResponseRedirect(reverse('App_Event:event_list'))
    context ={'form': form}
    return render(request, 'App_ClubAdmin/signup_clubadmin.html', context)

def LoginView(request):
    form = LoginUser()
    if request.method == "POST":
        form = LoginUser(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in")
                return HttpResponseRedirect(reverse('App_Event:event_list'))
            else:
                messages.error(request, "Username or Password Incorrect")
    context = {'form': form}
    return render(request, 'App_ClubAdmin/login_page.html', context)

@login_required
def LogoutView(request):
    logout(request)
    messages.success(request, "You have been logged out successfully!")
    return HttpResponseRedirect(reverse('App_Event:event_list'))