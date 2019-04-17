from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'events/home.html')


def events(request):
    return render(request, 'events/events.html')


def new_event(request):
    return render(request, 'events/new_event.html')