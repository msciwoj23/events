from django import forms
from oa.models import activity


class ActivityForm(forms.ModelForm):
	class Meta:
		model = activity
		fields = ['title', 'type', 'description']
