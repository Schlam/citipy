import pandas as pd
import numpy as np


# load the city data up

os.path.join(os.getcwd(), 'citypy', 'worldcities.csv')
df = pd.read_csv(_world_cities_csv_path)

# Function for finding nearest city
def nearest_city(latitude, longitude):
    lats = df.Latitude
    lons = df.Longitude
    index = np.sqrt((lats - latitude) ** 2 + (lons - longitude) ** 2).argmin()
    return df.iloc[index, 0]