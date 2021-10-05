from django.db import models
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from App_ClubAdmin.models import ClubAdmin
from App_Volunteer.models import Volunteer

from django.contrib.auth import get_user_model


User = get_user_model()
# Create your models here.

class Event(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='clubadmin_event_created')
    event_title = models.CharField(max_length=150, verbose_name="Event Title")
    description = models.TextField(max_length=1000, verbose_name="Event Description")
    venue = models.CharField(max_length=60)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    fee_required = models.BooleanField(default=False, blank=True)
    registration_fee = models.FloatField(default=0.00, blank=True)
    registration_deadline = models.DateTimeField(blank=True, null=True)
    registration_status = models.BooleanField(default=False)
    event_banner = models.ImageField(upload_to="Event/%Y/%m/%d/")
    event_link = models.URLField(max_length=255, blank=True, null=True)
    event_fb_link = models.URLField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = [ '-date_created' ]

    def __str__(self):
        return self.event_title

class EventNotice(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="events_notice")
    event_notice = models.TextField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.event_notice

class EventPhoto(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="events_photo")
    event_photo = models.ImageField(upload_to="EventsPhoto/%Y/%m/%d/", blank =True)

class EventVolunteer(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="events_volunteer")
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE, related_name="event_volunteers")

    def __str__(self):
        return self.volunteer.user.username
