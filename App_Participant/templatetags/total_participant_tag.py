from django import template
from App_Event.models import Event
from App_Participant.models import Participant

register = template.Library()


@register.filter
def total_participant(id):
    event = Event.objects.get(event_id=id, is_active=True)
    participants = Participant.objects.filter(event=event)
    for participant in participants:
        if participant.participant.payment_status == True:
            pass
    return None
