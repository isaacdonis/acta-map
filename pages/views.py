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
        # descriptions_values = []
        # id_values = []
        # id = 0
        for station in subway_station_locations:
            # id += 1
            lat = station.lat
            lon = station.lon
            # descrip = self.clean_descrip(station.shortdescription)
            # els = self.clean_elevators(station.equipmentno)

            # split_desc = descrip.split(",")
            # split_els = els.split(",")
            # total_desc = " | ".join([x.strip(r"'") + ": " + y.strip(r"'") for x,y in zip(split_els, split_desc)])

            lat_values.append(lat)
            lon_values.append(lon)
            # descriptions_values.append(total_desc)
            # id_values.append(id)

        context = super().get_context_data(**kwargs)
        context["lat"] = lat_values
        context["lon"] = lon_values

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