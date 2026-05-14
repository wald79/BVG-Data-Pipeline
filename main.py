from src.extract import extract_station, extract_departure
from src.transform import transform_stop, transform_departure
from src.load import load_to_postgres

def main():
    #stop = input("Enter the name of the stop: ")
    with open('stops.txt','r') as file:
        stop = file.readlines()
        for s in stop:
            station_data = extract_station(s.strip())
            
            if station_data:
                transformed_station = transform_stop(station_data)
                load_to_postgres("stations", transformed_station)

                departure_data = extract_departure(station_data[0].get('id'))
                
                if departure_data:
                    transformed_departure = transform_departure(departure_data)
                    load_to_postgres("departures", transformed_departure)
            else:
                print("No station data to process.")

if __name__ == "__main__":
    main()