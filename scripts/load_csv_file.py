from pages.models import SubwayStations
import csv

def run():
    with open('pages/subway_stations.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        SubwayStations.objects.all().delete()

        for row in reader:
            print(row)

            subway_stations = SubwayStations(lat=row[0],
                        lon=row[1])
            
            subway_stations.save()