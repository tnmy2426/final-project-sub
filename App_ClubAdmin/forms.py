from django import forms
from django.db import models
from django.db.models import fields
from .models import User, ClubAdmin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CreateNewUser(UserCreationForm):
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={"placeholder": "UG02-00-00-000"}))
    full_name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={"placeholder": "Full Name"}))
    password1 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={"placeholder": "Password"}))
    password2 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={"placeholder": "Password Confirmation"}))
    class Meta:
        model = User
        fields = ('username', 'full_name', 'password1', 'password2', )


class LoginUser(AuthenticationForm):
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={"placeholder": "UG02-00-00-000"}))
    password = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={"placeholder": "Password"}))

    error_messages = {
        'invalid_login':(
            "Your are not authorized or verified yet!!"
        ),
        'inactive':("This account is inactive."),
    }
    class Meta:
        model = User
        fields = ('username', 'password')

class ClubAdminProfileForm(forms.ModelForm):
    class Meta:
        model = ClubAdmin
        fields = ("designation", "gender", "phone_no", "address", "fb_id_link")

class ProfilePicUpload(forms.ModelForm):
    class Meta:
        model = ClubAdmin
        fields = ("profile_pic",)