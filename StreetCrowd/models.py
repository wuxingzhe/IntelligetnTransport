from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class CarStatus(models.Model):
    car_id=models.IntegerField()
    longitude = models.FloatField()
    latitude=models.FloatField()
    speed=models.FloatField(default=0.0)
    timeID=models.IntegerField(default=0)
    timeID.db_index=True

    def __str__(self):
        return str(self.car_id)+' '+str(self.longitude)+' '+str(self.latitude)+' '+str(self.speed)+' '+str(self.timeID)
