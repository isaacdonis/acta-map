from django.core.validators import MaxValueValidator
from django.db import models
from django.urls import reverse


class SubwayStation(models.Model):
    station_id = models.IntegerField(validators=[MaxValueValidator(523)], default=-1)
    complex_id = models.IntegerField(null=False, default=-1)
    gtfs_stop_id = models.CharField(
        null=False, blank=False, max_length=700, default="No information available"
    )
    division = models.CharField(
        null=False, blank=False, max_length=700, default="No information available"
    )
    line = models.CharField(
        null=False, blank=False, max_length=700, default="No information available"
    )
    stop_name = models.CharField(
        null=False, blank=False, max_length=700, default="No information available"
    )
    borough = models.CharField(
        null=False, blank=False, max_length=700, default="No information available"
    )
    daytime_routes = models.CharField(
        null=False, blank=False, max_length=700, default="No information available"
    )
    structure = models.CharField(
        null=False, blank=False, max_length=700, default="No information available"
    )
    gtfs_latitude = models.CharField(
        null=False, blank=False, max_length=700, default="No information available"
    )
    gtfs_longitude = models.CharField(
        null=False, blank=False, max_length=700, default="No information available"
    )
    north_direction_label = models.CharField(
        null=False, blank=False, max_length=700, default="No information available"
    )
    south_direction_label = models.CharField(
        null=False, blank=False, max_length=700, default="No information available"
    )
    ada = models.IntegerField(validators=[MaxValueValidator(2)], default=-1)
    ada_notes = models.CharField(
        null=False, blank=False, max_length=700, default="No information available"
    )
    georeference = models.CharField(
        null=False, blank=False, max_length=700, default="No information available"
    )
    lon = models.FloatField(null=False, blank=False, default=-1)
    lat = models.FloatField(null=False, blank=False, default=-1)

    def __str__(self):
        return f"{self.stop_name} -- {self.lat},{self.lon}"

    def get_absolute_url(self):
        return reverse("stationfeedback", kwargs={"pk": self.pk})


class Feedback(models.Model):
    station = models.ForeignKey(SubwayStation, on_delete=models.PROTECT)
    text = models.TextField()

    def __str__(self):
        return f"{self.station} - {self.text}"
