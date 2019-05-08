from django.shortcuts import render
from django.http import HttpResponse


from .forms import EventForm
from .models import event


# Create your views here.
def home(request):
    return render(request, 'events/home.html')


def events(request):
    return render(request, 'events/events.html')


def new_event(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'events/new_event.html', context)