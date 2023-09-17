from django.db import models

# Create your models here.
class SubwayStations(models.Model):
    lat = models.FloatField(null=False,blank=False)
    lon = models.FloatField(null=False, blank=False)

    def __str__(self):
        return f"{self.lat},{self.lon}"