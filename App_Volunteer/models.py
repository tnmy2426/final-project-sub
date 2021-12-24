from django.db import models
from django.conf import settings

# Create your models here.

class Volunteer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="volunteer_user")
    phone_no = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.user.full_name
    