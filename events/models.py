from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import ForeignKey

class User(models.Model):
    user_id: int = models.AutoField(primary_key=True)
    login: str = models.CharField(max_length=200)
    password: str = models.CharField(max_length=200)
    first_name: str = models.CharField(max_length=200)
    last_name: str = models.CharField(max_length=200)
    nickname: str = models.CharField(max_length=200)
    email: str = models.CharField(max_length=200)
    isAdmin: bool = models.BooleanField()

    def __str__(self):
        return self.first_name



class EventStatus(models.Model):
    event_status_id: int = models.AutoField(primary_key=True)
    event_status_name: str = models.TextField(max_length=200)

    class Meta:
        db_table = 'events_event_status'

    def __str__(self):
        return self.event_status_name


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name: str = models.CharField(max_length=200)
    user_id: ForeignKey = ForeignKey(User, on_delete=models.CASCADE)
    event_status_id: ForeignKey = models.ForeignKey(EventStatus, on_delete=models.CASCADE)
    place: str = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    deadline_date = models.DateField()
    description = models.CharField(max_length=200)
    date_of_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'events_event'

    def __str__(self):
        return self.event_name



class Activity(models.Model):
    activity_id: int = models.AutoField(primary_key=True)
    event_id: ForeignKey = models.ForeignKey('events.Event', on_delete=models.CASCADE)
    user_id: ForeignKey = models.ForeignKey('events.User', on_delete=models.CASCADE)
    # activity_status_id: ForeignKey = models.ForeignKey('events.ActivityStatus', on_delete=models.CASCADE)
    title: str = models.TextField(max_length=200)
    type: str = models.TextField(max_length=200)
    description: str = models.TextField(max_length=200)
    duration = models.DateField()
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ActivityStatus(models.Model):
    activity_status_id: int = models.AutoField(primary_key=True)
    activity_status_name: str = models.TextField(max_length=200)

    class Meta:
        db_table = 'events_activity_status'

    def __str__(self):
        return self.activity_status_name


class Message(models.Model):
    message_id: int = models.AutoField(primary_key=True)
    # user_id: ForeignKey = models.ForeignKey('events.User', on_delete=models.CASCADE)
    # activity_id: ForeignKey = models.ForeignKey('events.Activity', on_delete=models.CASCADE)
    created = models.DateField()
    message = models.TextField(max_length=200)
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message


class Tag(models.Model):
    tag_id: int = models.AutoField(primary_key=True)
    tag_name: str = models.TextField(max_length=200)

    def __str__(self):
        return self.tag_name


class TagActivity(models.Model):
    activities_id: [] = ArrayField(models.IntegerField(primary_key=True))
    tag_id: int = models.BigIntegerField()

    def __str__(self):
        return str(self.tag_id)

