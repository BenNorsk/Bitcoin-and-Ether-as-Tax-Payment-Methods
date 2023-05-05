import pandas as pd
import json
import re
import matplotlib.pyplot as plt

# Get the plz from the json file

def read_plz(data_dict):
    try:
        address = data_dict["candidates"][0]
        formatted_address = address["formatted_address"]
    except:
        return None
    plz = re.search(r"\d\d\d\d", formatted_address)
    if plz is not None:
        return plz.group(0)
    return None

# Get the country from the json file

def read_country(data_dict):
    try:
        address = data_dict["candidates"][0]
        formatted_address = address["formatted_address"]
    except:
        return None
    country = formatted_address.split(",")[-1].strip()
    return country

# Get the canton from the plz

def read_canton(data_dict, cantons):
    try:
        address = data_dict["candidates"][0]
        formatted_address = address["formatted_address"]
    except:
        return None
    # Try if the fomratted address contains a canton
    for key in cantons:
        # Split by space, colon, point or comma without using the key
        words = re.split(r"[\s\.,:]", formatted_address)
        if key in words:
            canton = cantons[key]
            return canton
    return None

def read_lat(data_dict):
    try:
        address = data_dict["candidates"][0]
        geometry = address["geometry"]
        location = geometry["location"]
        lat = location["lat"]
        return lat
    except:
        return None

def read_lng(data_dict):
    try: 
        address = data_dict["candidates"][0]
        geometry = address["geometry"]
        location = geometry["location"]
        lng = location["lng"]
        return lng
    except:
        return None

def read_address(data_dict):
    try:
        address = data_dict["candidates"][0]
        formatted_address = address["formatted_address"]
        return formatted_address
    except:
        return None
        

def read_json(id, cantons):
    with open(f'places/{id}.json', 'r') as f:
        json_data = f.read()
    # Replace single with double quotes
    try:
        json_data = json_data.replace("'", '"')
        data_dict = json.loads(json_data)
    except:
        return None
    country = read_country(data_dict)
    plz = read_plz(data_dict)
    canton = read_canton(data_dict, cantons)
    lat = read_lat(data_dict)
    lng = read_lng(data_dict)
    address = read_address(data_dict)
    data = {
        "id": id,
        "address": address,
        "country": country,
        "plz": plz,
        "canton": canton,
        "lat": lat,
        "lng": lng
    }
    return data


def main():
    df = pd.read_pickle("main.pkl")
    df_location = pd.DataFrame(columns=["id", "address", "country", "plz", "canton", "lat", "lng"])

    # read the look_up.json as a dictionary
    with open("look_up.json", "r") as f:
        cantons = f.read()
        # Make the string a dictionary
        cantons = json.loads(cantons)
    for index, row in df.iterrows():
        id = row["id"]
        data_row = read_json(id, cantons)
        # Concat the data row to the dataframe
        df_location = pd.concat([df_location, pd.DataFrame([data_row])], ignore_index=True)
    # Delete all rows, where country is not Switzerland
    df_location = df_location[df_location["country"] == "Schweiz"]
    # Drop the column "0"
    df_location = df_location.drop(columns=[0])
    # Save the dataframe as a pickle file
    df_location.to_pickle("location.pkl")
    # Save the dataframe as a csv file
    df_location.to_csv("location.csv", index=False)
   

if __name__ == "__main__":
    main()
