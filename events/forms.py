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
        # widgets = {
        #     'start_date': DateField(attrs={'hidden':True}),
        #     'end_date': DateField(attrs={'hidden':True}),
        #     'deadline_date': DateField(attrs={'hidden':True})
        # }