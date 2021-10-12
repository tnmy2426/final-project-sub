from django import template
from django.shortcuts import get_object_or_404
from App_Event.models import Event
from App_Participant.models import Participant, ParticipantStatus

register = template.Library()


@register.filter
def verified_participant(id):
    event = get_object_or_404(Event, id=id)
    participants = Participant.objects.filter(event=event, payment_status=True)
    return participants.count()


@register.filter
def total_attendence(id):
    event= get_object_or_404(Event, id=id)
    status = ParticipantStatus.objects.filter(event=event, payment_status=True, attendence=True)
    return status.count()

@register.filter
def available_kit_token(id):
    event= get_object_or_404(Event, id=id)
    status = ParticipantStatus.objects.filter(event=event, payment_status=True, kit_token=False)
    return status.count()

@register.filter
def available_misc_token(id):
    event= get_object_or_404(Event, id=id)
    status = ParticipantStatus.objects.filter(event=event, payment_status=True, misc_token=False)
    return status.count()

@register.filter
def available_breakfast_token(id):
    event= get_object_or_404(Event, id=id)
    status = ParticipantStatus.objects.filter(event=event, payment_status=True, breakfast_token=False)
    return status.count()

@register.filter
def available_lunch_token(id):
    event= get_object_or_404(Event, id=id)
    status = ParticipantStatus.objects.filter(event=event, payment_status=True, lunch_token=False)
    return status.count()

@register.filter
def available_snacks_token(id):
    event= get_object_or_404(Event, id=id)
    status = ParticipantStatus.objects.filter(event=event, payment_status=True, snacks_token=False)
    return status.count()