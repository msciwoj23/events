from django.db import models
from django.contrib.postgres.fields import ArrayField


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=200)
    owner_id = models.BigIntegerField()
    event_status_id = models.BigIntegerField()
    place = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    deadline_date = models.DateField()
    description = models.CharField(max_length=200)
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_name


class EventStatus(models.Model):
    event_status_id = models.BigIntegerField(primary_key=True)
    event_status_name = models.TextField(max_length=200)

    def __str__(self):
        return self.event_status_name


class Activity(models.Model):
    activity_id = models.BigIntegerField(primary_key=True)
    event_id = models.BigIntegerField()
    author_id = models.BigIntegerField()
    activity_status_id = models.BigIntegerField()
    title = models.TextField(max_length=200)
    type = models.TextField(max_length=200)
    description = models.TextField(max_length=200)
    duration = models.DateField()
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ActivityStatus(models.Model):
    activity_status_id = models.BigIntegerField(primary_key=True)
    activity_status_name = models.TextField(max_length=200)

    def __str__(self):
        return self.activity_status_name


class Message(models.Model):
    message_id = models.BigIntegerField(primary_key=True)
    author_id = models.BigIntegerField()
    activity_id = models.BigIntegerField()
    created = models.DateField()
    message = models.TextField(max_length=200)
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message


class Tag(models.Model):
    tag_id = models.BigIntegerField(primary_key=True)
    tag_name = models.TextField(max_length=200)

    def __str__(self):
        return self.tag_name


class TagActivity(models.Model):
    activities_id = ArrayField(models.IntegerField())
    tag_id = models.BigIntegerField()

    def __str__(self):
        return str(self.tag_id)


class User(models.Model):
    user_id = models.BigIntegerField()
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    isAdmin = models.BooleanField()
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
