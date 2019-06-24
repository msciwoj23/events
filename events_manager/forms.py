from django.forms import ModelForm, DateField
from django import forms

from .models import Event, Activity, User, EventStatus


common_input_format_Datefield = forms.DateField(
                                 input_formats=('%d/%m/%Y',))


class DateInput(forms.DateInput):
    input_type = 'date'


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
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
            'deadline_date': DateInput(),
        }


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