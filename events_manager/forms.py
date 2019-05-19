from django.forms import ModelForm, DateField

from .models import Event, Activity, User, EventStatus


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


class UserForm(ModelForm):
    class Meta:
        model = User
        exclude = ('user_id',)


class EventStatusForm(ModelForm):
    class Meta:
        model = EventStatus
        exclude = ('event_status_id',)