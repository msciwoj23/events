from django.db import models
from django.contrib.postgres.fields import ArrayField


class event(models.Model):
    event_id = models.BigIntegerField()
    event_name: str = models.CharField(max_length=200)
    owner_id = models.BigIntegerField()
    event_status_id = models.BigIntegerField()
    place: str = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    deadline_date = models.DateField()
    description: str = models.CharField(max_length=200)

    def __str__(self):
        return self.description


class event_status(models.Model):
    event_status_id: int = models.BigIntegerField(primary_key=True)
    event_status_name: str = models.TextField(max_length=200)

    def __str__(self):
        return self.event_status_name


class activity(models.Model):
    activity_id: int = models.BigIntegerField(primary_key=True)
    event_id: int = models.BigIntegerField()
    author_id: int = models.BigIntegerField()
    activity_status_id: int = models.BigIntegerField()
    title: str = models.TextField(max_length=200)
    type: str = models.TextField(max_length=200)
    description: str = models.TextField(max_length=200)
    duration = models.DateField()

    def __str__(self):
        return self.title

class activity_status(models.Model):
    activity_status_id: int = models.BigIntegerField(primary_key=True)
    activity_status_name: str = models.TextField(max_length=200)

    def __str__(self):
        return self.activity_status_name


class message(models.Model):
    message_id: int = models.BigIntegerField(primary_key=True)
    author_id: int = models.BigIntegerField()
    activity_id: int = models.BigIntegerField()
    created = models.DateField()
    message: str = models.TextField(max_length=200)

    def __str__(self):
        return self.message


class tag(models.Model):
    tag_id: int = models.BigIntegerField(primary_key=True)
    tag_name: str = models.TextField(max_length=200)

    def __str__(self):
        return self.tag_name


class tag_activity(models.Model):
    activities_id: [] = ArrayField(models.IntegerField())
    tag_id: int = models.BigIntegerField()

    def __str__(self):
        return str(self.tag_id)


class user(models.Model):
    user_id = models.BigIntegerField()
    login: str = models.CharField(max_length=200)
    password: str = models.CharField(max_length=200)
    first_name: str = models.CharField(max_length=200)
    last_name: str = models.CharField(max_length=200)
    nickname: str = models.CharField(max_length=200)
    email: str = models.CharField(max_length=200)
    isAdmin: bool = models.BooleanField()

    def __str__(self):
        return self.first_name