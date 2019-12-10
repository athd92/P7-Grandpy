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

        gmaps = googlemaps.Client(key='AIzaSyCEp0QNbJZn4GZYVzSCn3xjwAQgzNq7KHk')
        # Geocoding an address
        geocode_result = gmaps.geocode(self.query)
        return geocode_result
  
    