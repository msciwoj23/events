from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='events-home'),
    path('events/', views.events, name='events-events'),
    path('new_event/', views.new_event, name='events-new_event'),
]