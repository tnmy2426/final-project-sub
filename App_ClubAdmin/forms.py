from django import forms
from .models import User
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