from django.forms import ModelForm, DateField
from django.conf import settings

from .models import Event

my_date_formats = [
                 '%d-%m-%Y',
                 '%d/%m/%Y',
                 '%d.%m.%Y']


class EventForm(ModelForm):
    start_date = DateField(input_formats=settings.NORMAL_DATE_FORMATS)
    end_date = DateField(input_formats=settings.NORMAL_DATE_FORMATS)
    deadline_date = DateField(input_formats=settings.NORMAL_DATE_FORMATS)
    class Meta:
        model = Event
        exclude = ['event_id']