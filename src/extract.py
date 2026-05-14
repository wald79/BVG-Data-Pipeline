import requests

def extract_station(stop):
    url = f"https://v6.bvg.transport.rest/locations?poi=false&addresses=false&query={stop}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        
        if not data:
            print("No results found.")
            return None
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")



def extract_departure(id):
    url = f"https://v6.bvg.transport.rest/stops/{id}/departures?results=2"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        
        if not data:
            print("No results found.")
            return None
        
        return data


    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

#dep = extract_departure(station['id'])
#print(dep)