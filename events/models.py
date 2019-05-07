from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models import ForeignKey


class event(models.Model):
    event_id = models.BigIntegerField(primary_key=True)
    event_name: str = models.CharField(max_length=200)
    user_id: ForeignKey = ForeignKey('user', on_delete=models.CASCADE)
    event_status_id: ForeignKey = models.ForeignKey('event_status', on_delete=models.CASCADE)
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
    event_id: ForeignKey = models.ForeignKey('event', on_delete=models.CASCADE)
    user_id: ForeignKey = models.ForeignKey('user', on_delete=models.CASCADE)
    activity_status_id: ForeignKey = models.ForeignKey('activity_status', on_delete=models.CASCADE)
    title: str = models.TextField(max_length=200)
    type: str = models.TextField(max_length=200)
    description: str = models.TextField(max_length=200)
    duration = models.DateField()

    @property
    def __str__(self):
        return self.title


class activity_status(models.Model):
    activity_status_id: int = models.BigIntegerField(primary_key=True)
    activity_status_name: str = models.TextField(max_length=200)

    def __str__(self):
        return self.activity_status_name


class message(models.Model):
    message_id: int = models.BigIntegerField(primary_key=True)
    user_id: ForeignKey = models.ForeignKey('user', on_delete=models.CASCADE)
    activity_id: ForeignKey = models.ForeignKey('activity', on_delete=models.CASCADE)
    created = models.DateField()
    message: str = models.TextField(max_length=200)

    def __str__(self):
        return self.message


class tag(models.Model):
    tag_id: int = models.BigIntegerField(primary_key=True)
    tag_name: str = models.TextField(max_length=200)

    def __str__(self):
        return self.tag_name


# class tag_activity(models.Model):
#     activities_id: [] = ArrayField(models.IntegerField(primary_key=True))
#     tag_id: int = models.BigIntegerField()
#
#     def __str__(self):
#         return str(self.tag_id)


class user(models.Model):
    user_id: int = models.BigIntegerField(primary_key=True)
    login: str = models.CharField(max_length=200)
    password: str = models.CharField(max_length=200)
    first_name: str = models.CharField(max_length=200)
    last_name: str = models.CharField(max_length=200)
    nickname: str = models.CharField(max_length=200)
    email: str = models.CharField(max_length=200)
    isAdmin: bool = models.BooleanField()

    def __str__(self):
        return self.first_name