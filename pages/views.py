import json
import random
from typing import Any, Dict

from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, TemplateView

from .models import Feedback, SubwayStation


class HomePageView(ListView):
    """
    The format that this data needs to be in is:

    const clearances = {
        type: 'FeatureCollection',
        features: [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [-74.07515140286641, 40.581379513893616]
                },
                "properties": {
                    "clearance": "13'2"
                }
            }
        ]
    }
    """

    model = SubwayStation
    template_name = "home.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        # get the subway location that is in the database
        subway_station_locations = SubwayStation.objects.all()

        object_ids = []
        lat_values = []
        lon_values = []
        stop_names = []
        line_names = []
        ada_values = []

        for station in subway_station_locations:
            lat = station.lat
            lon = station.lon
            stop_name = station.stop_name
            line = station.line
            ada = station.ada

            object_ids.append(station.pk)
            lat_values.append(lat)
            lon_values.append(lon)
            stop_names.append(stop_name)
            line_names.append(line)
            ada_values.append(ada)

        context = super().get_context_data(**kwargs)
        context["object_ids"] = object_ids
        context["lat"] = lat_values
        context["lon"] = lon_values
        context["stop_name"] = stop_names
        context["line_name"] = line_names
        context["adas"] = ada_values

        return context

    def clean_descrip(self, descrip):
        descrip = descrip.strip("()")

        return descrip

    def clean_elevators(self, el_str):
        return el_str.strip("()")


# class StationFeedback(DetailView, UpdateView):
#     model = SubwayStation
#     fields = ["community_feedback"]
#     template_name = "station_feedback.html"


def station_feedback(request, pk):
    station = get_object_or_404(SubwayStation, pk=pk)

    if request.method == "POST":
        Feedback.objects.create(station=station, text=request.POST["feedback"])

    return render(request, "station_feedback.html", {"station": station})


class ContactPage(TemplateView):
    template_name = "contact.html"


class AboutPage(TemplateView):
    template_name = "about.html"
