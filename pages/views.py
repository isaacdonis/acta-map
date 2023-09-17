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

        subway_location_dict = dict()
        subway_location_dict["trees"] = {"type":"FeatureCollection",
                                            "features":[]}
    
        # get the subway location that is in the database
        subway_station_locations = SubwayStations.objects.all()

        for station in subway_station_locations:
            lat = station.lat
            lon = station.lon

            features_dict = dict()
            features_dict["type"] = "Feature"
            features_dict["geometry"] = {"type":"Point", "coordinates":[lon,lat]}

            subway_location_dict["trees"]["features"].append(features_dict)

        context = super().get_context_data(**kwargs)
        context["points"] = subway_location_dict

        return context