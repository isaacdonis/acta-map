import random
import json
from typing import Any, Dict, Optional

from django.db import models
from .models import SubwayStations
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView

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

    model = SubwayStations
    template_name = "home.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:

        # get the subway location that is in the database
        subway_station_locations = SubwayStations.objects.all()

        lat_values = []
        lon_values = []
        stop_names = []
        line_names = []

        for station in subway_station_locations:
            lat = station.lat
            lon = station.lon
            stop_name = station.stop_name
            line = station.line

            lat_values.append(lat)
            lon_values.append(lon)
            stop_names.append(stop_name)
            line_names.append(line)

        context = super().get_context_data(**kwargs)
        context["lat"] = lat_values
        context["lon"] = lon_values
        context["stop_name"] = stop_names
        context["line_name"] = line_names

        return context
    
    def clean_descrip(self, descrip):
        
        descrip = descrip.strip("()")

        return descrip
    
    def clean_elevators(self, el_str):

        return el_str.strip("()")

class StationFeedback(DetailView, UpdateView):
    model = SubwayStations
    fields = ["community_feedback"]
    template_name = "station_feedback.html"

class ContactPage(TemplateView):
    template_name = "contact.html"

class AboutPage(TemplateView):
    template_name = "about.html"