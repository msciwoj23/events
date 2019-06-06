from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


from .forms import EventForm, ActivityForm, UserForm, EventStatusForm
from .models import Event, Activity


def home(request):
    event_list = Event.objects.order_by('-start_date')[:5]
    context = {'event_list': event_list}
    return render(request, 'events/home.html', context)


def events(request):
    event_list = Event.objects.order_by('-start_date')
    context = {'event_list': event_list}
    return render(request, 'events/events.html', context)


def event_details(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    activities_list = Activity.objects.filter(event=event).order_by('-start_date')[::-1]
    context = {'event': event, 'activities_list' : activities_list }
    return render(request, 'events/event_details.html', context)


def activities(request):
    activity_list = Activity.objects.order_by('-title')
    context = {'activity_list': activity_list}
    return render(request, 'events/activities.html', context)


def new_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(request.FILES)
            # return redirect('home')
    else:
        form = EventForm()
    return render(request, 'events/new_event.html', {
        'form': form
    })

    # form = EventForm(request.POST, request.FILES)
    #
    # if form.is_valid():
    #     form.save()
    # context = {
    #     'form': form
    # }
    # return render(request, 'events/new_event.html', context)


def new_activity(request):
    form = ActivityForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        print("ERROR!")
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
