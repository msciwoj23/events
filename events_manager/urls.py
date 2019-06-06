from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='events_manager-home'),
    path('events_manager/', views.events, name='events_manager-events_manager'),
    path('event_details/<int:event_id>/', views.event_details, name='events_manager-event_details'),
    path('activities/', views.activities, name='events_manager-activities'),
    path('new_event/', views.new_event, name='events_manager-new_event'),
    path('new_activity/', views.new_activity, name='events_manager-new_activity'),
    path('new_user/', views.new_user, name='events_manager-new_user'),
    path('new_event_status/', views.new_event_status, name='events_manager-new_event_status'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)