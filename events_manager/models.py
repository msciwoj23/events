from django.db import models
from django.db.models import ForeignKey


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    isAdmin = models.BooleanField()

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.first_name


class EventStatus(models.Model):
    event_status_id = models.AutoField(primary_key=True)
    event_status_name = models.TextField(max_length=200)

    class Meta:
        db_table = 'event_status'

    def __str__(self):
        return self.event_status_name


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=200)
    user = ForeignKey(User, on_delete=models.CASCADE)
    event_status = models.ForeignKey(EventStatus, on_delete=models.CASCADE)
    place = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    deadline_date = models.DateField()
    description = models.CharField(max_length=200)

    class Meta:
        db_table = 'event'

    def __str__(self):
        return self.event_name


class ActivityStatus(models.Model):
    activity_status_id = models.AutoField(primary_key=True)
    activity_status_name = models.TextField(max_length=200)

    class Meta:
        db_table = 'activity_status'

    def __str__(self):
        return self.activity_status_name


class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_status = models.ForeignKey(ActivityStatus, on_delete=models.CASCADE)
    title = models.TextField(max_length=200)
    activity_type = models.TextField(max_length=200)
    description = models.TextField(max_length=200)
    time = models.DateTimeField()
    duration = models.DateField()
    place = models.CharField(max_length=200)


    class Meta:
        db_table = 'activity'

    def __str__(self):
        return self.title


class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    created = models.DateField()
    message = models.TextField(max_length=200)

    class Meta:
        db_table = 'message'

    def __str__(self):
        return self.message


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.TextField(max_length=200)
    activities = models.ManyToManyField(Activity)

    class Meta:
        db_table = 'tag'

    def __str__(self):
        return self.tag_name


