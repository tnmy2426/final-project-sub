from django.db import models
from App_Event.models import Event


# Create your models here.

class Participant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event_participant")
    event_reg_id = models.CharField(max_length=20, blank=False)
    participant_name = models.CharField(max_length=20, blank=False)
    participant_email = models.EmailField(max_length=254, blank=False)
    phone_no = models.CharField(max_length=20, blank=False)
    guests = models.IntegerField(blank=True, default=0, null=True)
    fee_amount = models.FloatField(default=0.00)
    payment_status = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.participant_name}"
class ParticipantStatus(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event_participantstatus")
    participant = models.OneToOneField(Participant, on_delete=models.CASCADE, related_name="participant_status")
    attendence = models.BooleanField(default=False)
    payment_status = models.BooleanField(default=False)
    payment_amount = models.FloatField(default=0.00)
    transaction_id = models.CharField(max_length=20, blank=True)
    kit_token = models.BooleanField(default=False)
    breakfast_token = models.BooleanField(default=False)
    lunch_token = models.BooleanField(default=False)
    snacks_token = models.BooleanField(default=False)
    misc_token = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Participant Status"

    def __str__(self):
        return self.participant.participant_name
    