from django.core.validators import MaxValueValidator
from django.db import models
from django.urls import reverse


# Create your models here.
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
    community_feedback = models.TextField(
        null=False,
        blank=False,
        default="Enter advice to the community about this station here.",
    )
    all_comm_feedback = models.TextField(
        null=True,
        blank=False,
        default="Community feedback will appear below here when you fill out the form below",
    )

    def __str__(self):
        return f"{self.lat},{self.lon}"

    def get_absolute_url(self):
        return reverse("stationfeedback", kwargs={"pk": self.pk})

    def list_feedback_items(self):
        return self.all_comm_feedback.split("\n")

    def save(self, *args, **kwargs):
        self.all_comm_feedback = (
            self.all_comm_feedback + "\n" + self.community_feedback.strip()
        )
        self.all_comm_feedback = self.all_comm_feedback.strip()

        super(SubwayStation, self).save(*args, **kwargs)
