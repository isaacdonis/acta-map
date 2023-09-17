from django.db import models

# Create your models here.
class SubwayStations(models.Model):
    lon = models.FloatField(null=False, blank=False)
    lat = models.FloatField(null=False,blank=False)

    def __str__(self):
        return f"{self.lat},{self.lon}"