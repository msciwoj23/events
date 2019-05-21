from django.shortcuts import render
from django.http import HttpResponse


from .forms import EventForm, ActivityForm, UserForm, EventStatusForm
from .models import Event, Activity


# Create your views here.
def home(request):
    return render(request, 'events/home.html')


def events(request):
    event_list = Event.objects.order_by('-start_date')
    print(event_list)
    context = {'event_list' : event_list}
    return render(request, 'events/events.html', context)


def activities(request):
    return render(request, 'events/activities.html')


def new_event(request):
    form = EventForm(request.POST or None)
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
