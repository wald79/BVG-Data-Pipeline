import json
import pandas as pd

def transform_departure(data):
 
    try:
        departures = data.get("departures", [])

        result = []
  
        for d in departures:
            result.append({                
            "trip_id": d.get("tripId"),
            "station_id": d.get("stop", {}).get("id"),
            "station_name": d.get("stop", {}).get("name"),
            "delay": d.get("delay"),
            "line": d.get("line", {}).get("name"),
            "direction": d.get("direction")
                })
        return result
    
    except Exception as e:
        print("Error in transforming data",e)

def transform_stop(data):

    try:
        result = []
        result.append({
            "station_id": data[0].get("id"),
            "station_name": data[0].get("name")
        })

        return result
    except Exception as e:
         print("Error in transforming data",e)