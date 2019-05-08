from django.forms import ModelForm, DateField

from .models import event


class EventForm(ModelForm):
    class Meta:
        model = event
        fields = (
            'event_name',
            'owner_id',
            'event_status_id',
            'place',
            'start_date',
            'end_date',
            'deadline_date',
            'description'
        )