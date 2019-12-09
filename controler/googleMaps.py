import os
import googlemaps
from datetime import datetime


class GoogleMaps:
    """
    Class used for the API REST request to the googlemaps
    """

    def __init__(self, query):
        self.query = query

    def get_geocode(self):
        """Method used to check the value of the maps infos initialized"""
        apiKey = os.environ.get('API_KEY_MAPS')
        gmaps = googlemaps.Client(apiKey)
        # Geocoding an address
        geocode_result = gmaps.geocode(self.query,  language='fr')
        return geocode_result
  
    