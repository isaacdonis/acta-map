import random
import json
from typing import Any, Dict
from .models import SubwayStations
from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
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
        descriptions = []
        for station in subway_station_locations:
            lat = station.lat
            lon = station.lon

            lat_values.append(lat)
            lon_values.append(lon)
            descriptions.append(json.dumps(random.sample(['This station has a narrow platform.', 
                                   'If  going towards Manhattan, turn left as you exit the train.',
                                   'There is an elevator, but it\'s typically always full between 4-6:30PM',
                                   'The elevator at this station is known to entrap people. The last entrapment was June 18th, 2022.'],1).pop()))

        context = super().get_context_data(**kwargs)
        context["lat"] = lat_values
        context["lon"] = lon_values
        context["descriptions"] = descriptions

        return context