from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='events_manager-home'),
    path('events_manager/', views.events, name='events_manager-events_manager'),
    path('new_event/', views.new_event, name='events_manager-new_event'),
    path('new_activity/', views.new_activity, name='events_manager-new_activity'),
    path('new_event_status/', views.new_event_status, name='events_manager-new_event_status'),
]