from django.forms import ModelForm, DateField

from .models import Event, Activity


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = (
            'event_name',
            'user_id',
            'event_status_id',
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
