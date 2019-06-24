import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Event

# from myapp.forms import MyForm
#
# class MyTests(TestCase):
#     def test_forms(self):
#         form_data = {'something': 'something'}
#         form = MyForm(data=form_data)
#         self.assertTrue(form.is_valid())


class EventModelTests(TestCase):

    def events_start_date_is_in_the_past(self):
        pass

    def events_start_date_is_too_soon(self):
        pass

    def events_end_date_is_in_the_past(self):
        pass

    def events_end_date_is_too_soon(self):
        pass

    def events_deadline_date_is_in_the_past(self):
        pass

    def events_deadline_date_is_too_soon(self):
        pass
