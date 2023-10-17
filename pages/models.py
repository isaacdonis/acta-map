from django.db import models

# Create your models here.
class SubwayStations(models.Model):
    lon = models.FloatField(null=False, blank=False)
    lat = models.FloatField(null=False,blank=False)
    shortdescription = models.CharField(null=False, blank=False, max_length=250, default="No information available")
    equipmentno = models.CharField(null=False, blank=False, max_length=250, default="No information available")

    def __str__(self):
        return f"{self.lat},{self.lon}"