from django.db import models
from django.conf import settings
from App_ClubAdmin.models import User
from App_Event.models import Event

# Create your models here.

class Volunteer(models.Model):
    Gender_Choices = [
        ("MALE", "Male"),
        ("FEMALE", "Female"),
        ("NONE", "None")
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="volunteer_user")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event_volunteer")
    gender = models.CharField(max_length=20, choices=Gender_Choices, default="NONE")
    phone_no = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.user.full_name
    