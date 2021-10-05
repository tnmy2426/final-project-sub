from django import forms
from django.contrib.auth import models
from django.db.models import fields
from .models import Event, EventPhoto, EventNotice
from App_Participant.models import Participant

class EventForm(forms.ModelForm):
    event_title = forms.CharField(required=True, label="Event Name")
    description = forms.CharField(required=True, label="Event Description", widget=forms.Textarea )
    venue = forms.CharField(required=True, label="Event Venue")
    start_datetime = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type':'datetime-local'}))
    end_datetime = forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type':'datetime-local'}))
    registration_deadline = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'type':'datetime-local'}))
    event_banner = forms.ImageField(label="Event Banner Photo")
    event_link = forms.URLField(label="Event Link", required=False)
    event_fb_link = forms.URLField(label="Event's Facebook Link", required=False)
    class Meta:
        model = Event
        fields = (
        "event_title", "description", "venue", "start_datetime", "end_datetime", "fee_required",
        "registration_fee", "registration_deadline", "event_banner", "event_link",
        "event_fb_link",
    )


class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = (
            "event_reg_id", "participant_name", "participant_email", "phone_no", "guests", "fee_amount", "transaction_id"
        )

class EventNoticeForm(forms.ModelForm):
    event_notice = forms.CharField(label="Event Notice", widget=forms.Textarea )
    class Meta:
        model = EventNotice
        fields = ("event_notice",)

class EventPhotoForm(forms.ModelForm):
    class Meta:
        model = EventPhoto
        fields = ("event_photo",)