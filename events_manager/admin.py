from django.contrib import admin

from .models import EventStatus, Event, Activity, ActivityStatus, User, Message, Tag

admin.site.register(EventStatus)
admin.site.register(Event)
admin.site.register(Activity)
admin.site.register(ActivityStatus)
admin.site.register(User)
admin.site.register(Message)
admin.site.register(Tag)


