from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse


from .forms import EventForm, ActivityForm, UserForm, EventStatusForm
from .models import Event, Activity


# Create your views here.
@login_required(login_url='/login')
def home(request):
    return render(request, 'events/home.html')

@login_required(login_url='/login')
def events(request):
     events = Event.objects.order_by('event_name')
     context = {'events': events}
     return render(request, 'events/events.html', context)


@login_required(login_url='/login')
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

@login_required(login_url='/login')
def new_activity(request):
    form = ActivityForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'events/new_activity.html', context)




@login_required(login_url='/login')
def new_event_status(request):
    form = EventStatusForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'events/new_event_status.html', context)
