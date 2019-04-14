from django.contrib import admin

from .models import event_status, event

admin.site.register(event_status)
admin.site.register(event)
