from django.shortcuts import render
import oa.models


def home(request):
	activity = oa.models.activity.objects.get(activity_id='0')
	print(activity)
	return render(request, 'home.html', {'activity': activity})
