from django.shortcuts import render
from django.http import HttpResponse


from .forms import EventForm, ActivityForm, UserForm, EventStatusForm
from .models import Event, Activity


# Create your views here.
def home(request):
    return render(request, 'events/home.html')


def events(request):
     events = Event.objects.order_by('event_name')
     context = {'events': events}
     return render(request, 'events/events.html', context)



def new_event(request):
    form = EventForm(request.POST or None)
    print('-------------------')
    print('BEGIN')
    print(form)
    print('END')
    print('-------------------')
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'events/new_event.html', context)


def new_activity(request):
    form = ActivityForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'events/new_activity.html', context)


def new_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'events/new_user.html', context)


def new_event_status(request):
    form = EventStatusForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'events/new_event_status.html', context)
