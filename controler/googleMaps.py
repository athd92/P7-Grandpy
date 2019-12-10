import googlemaps
from datetime import datetime
import os

class GoogleMaps:
    """
    Class used for the API REST request to the googlemaps
    """

    def __init__(self, query):
        self.query = query

    def get_geocode(self):
        """Method used to check the value of the maps infos initialized"""
        key = os.environ['API_KEY_MAPS']
        gmaps = googlemaps.Client(key)
        # Geocoding an address
        geocode_result = gmaps.geocode(self.query)
        return geocode_result
  
    