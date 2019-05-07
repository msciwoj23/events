from django.contrib import admin

from .models import event_status, event, activity, activity_status, user, message, tag

admin.site.register(event_status)
admin.site.register(event)
admin.site.register(activity)
admin.site.register(activity_status)
admin.site.register(user)
admin.site.register(message)
admin.site.register(tag)

