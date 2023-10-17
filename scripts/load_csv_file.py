from pages.models import SubwayStations
import csv
import os

def run():

    with open(os.path.join("pages","elevator_data.csv")) as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        SubwayStations.objects.all().delete()

        for row in reader:
            print(row)

            subway_stations = SubwayStations(lon=row[0],
                        lat=row[1],shortdescription=row[2], equipmentno=row[3])
            
            subway_stations.save()