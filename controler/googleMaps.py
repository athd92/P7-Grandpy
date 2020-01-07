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
        print('TEST')
        geocode_result = gmaps.geocode(self.query)
        if geocode_result == []:
            self.query = [self.query, 'france']
            geocode_result = gmaps.geocode(self.query)
            print(geocode_result)
        try:
            streetNumber = geocode_result[0]['address_components'][0]['short_name']
            streetName = geocode_result[0]['address_components'][1]['long_name']
            streetCity = geocode_result[0]['address_components'][2]['long_name']
            streetComplement = geocode_result[0]['address_components'][3]['long_name']

            address = streetNumber + '\
                ' + streetName + ' \
                ' + streetCity + ' \
                ' + streetComplement

            return geocode_result, address
        except ValueError:
            return geocode_result