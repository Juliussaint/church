from django.db import models


class Service(models.Model):
    unit_misioner = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()
    speaker = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='services/')



