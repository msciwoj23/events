from django.contrib.auth import authenticate
from django.shortcuts import render
from django.contrib.auth.models import User




# Create your views here.
from events_manager.forms import UserForm


def login(request):
    return render(request, 'registration/login.html')

def register(request):
    form = UserForm(request.POST or None)
    context = {
        'form': form
    }
    if request.method == 'POST' and form.is_valid():
        form.save()
        data = request.POST.copy()
        user = User.objects.create_user(username=data['login'], email=data['email'], password=data['password'])

    return render(request, 'registration/register.html', context)
