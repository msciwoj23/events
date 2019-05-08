from django.shortcuts import render
from .forms import ActivityForm
import oa.models


def review(request):
	activity = oa.models.activity.objects.all().values()
	form = ActivityForm()
	return render(request, 'review.html', {'activity': activity, 'form': form})






#
# def editActivity(request):
#     if request.method == 'POST':
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()
#
#     return render(request, 'name.html', {'form': form})
