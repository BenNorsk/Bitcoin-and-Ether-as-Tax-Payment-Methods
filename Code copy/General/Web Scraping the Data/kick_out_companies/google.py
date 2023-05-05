import pandas as pd
import re
import requests

API_KEY = 'AIzaSyCthuMbMMlgskygthCBhFj_2crnTo0YH0s'  # Replace with your Google Places API key

def get_place_info(place_name, id):
    # Construct the request URL
    url = f'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?key={API_KEY}&input={place_name}&inputtype=textquery&fields=formatted_address,geometry'

    # Send the request to the Google Places API
    response = requests.get(url)

    # Parse the JSON response
    json_data = response.json()

    # Save the JSON response to a file
    with open(f'places/{id}.json', 'w') as f:
        f.write(json_data)
    return 