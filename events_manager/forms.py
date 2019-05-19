from django.forms import ModelForm, DateField

from .models import Event, Activity


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = (
            'event_name',
            'user',
            'event_status',
            'place',
            'start_date',
            'end_date',
            'deadline_date',
            'description'
        )


class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        exclude = ('activity_id',)
