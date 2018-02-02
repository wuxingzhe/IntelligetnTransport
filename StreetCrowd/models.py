from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class CarStatus(models.Model):
    car_id=models.IntegerField()
    longitude = models.FloatField()
    latitude=models.FloatField()
    speed=models.IntegerField(default=0)
    direction=models.IntegerField(default=0)
    time=models.TimeField()

    def __str__(self):
        return str(self.car_id)+' '+str(self.longitude)+' '+str(self.latitude)

