from pages.models import SubwayStations
import csv
import os

def run():

    with open(os.path.join("pages","updated_subway_data.csv")) as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        SubwayStations.objects.all().delete()

        for row in reader:
            print(row)

            subway_stations = SubwayStations(station_id=row[0],
                        complex_id=row[1],
                        gtfs_stop_id=row[2],
                        division=row[3],
                        line=row[4],
                        stop_name=row[5],
                        borough=row[6],
                        daytime_routes=row[7],
                        structure=row[8],
                        gtfs_latitude=row[9],
                        gtfs_longitude=row[10],
                        north_direction_label=row[11],
                        south_direction_label=row[12],
                        ada=row[13],
                        ada_notes=row[14],
                        georeference=row[15],
                        lon=row[16],
                        lat=row[17],
                        community_feedback=row[18])
            
            subway_stations.save()