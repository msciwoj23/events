from django.contrib.auth import authenticate
from django.shortcuts import render





# Create your views here.
from events_manager.forms import UserForm


def login(request):
    return render(request, 'registration/login.html')

def register(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        form.save()

    context = {
            'form': form
        }
        # password = form.cleaned_data.get('password1')
        # user = authenticate(username=username, password=raw_password)
        # login(request, user)
    return render(request, 'registration/register.html', context)


