from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class CreateVolunteer(UserCreationForm):
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={"placeholder": "UG02-00-00-000"}))
    full_name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={"placeholder": "Enter Name"}))
    password1 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={"placeholder": "Password Confirmation"}))
    password2 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={"placeholder": "Password Confirmation"}))
    class Meta:
        model = User
        fields = ('username', 'full_name', 'password1', 'password2' )