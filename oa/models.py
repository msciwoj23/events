from django.db import models


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
