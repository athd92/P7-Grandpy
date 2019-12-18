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
        if geocode_result == []:
            self.query = [self.query, 'france']
            geocode_result = gmaps.geocode(self.query)
        try:
            streetNumber =
            geocode_result[0]['address_components'][0]['short_name']
            streetName =
            geocode_result[0]['address_components'][1]['long_name']
            streetCity =
            geocode_result[0]['address_components'][2]['long_name']
            streetComplement =
            geocode_result[0]['address_components'][3]['long_name']
            streetCityName =
            geocode_result[0]['address_components'][4]['long_name']
            streetCitySecondName =
            geocode_result[0]['address_components'][5]['long_name']
            streetCityCountry =
            geocode_result[0]['address_components'][6]['long_name']

            address =
            streetNumber + ' ' + streetName + ' ' + streetCity + ' '
            + streetComplement + ' ' + streetCityName + ' '
            + streetCitySecondName + ' ' + streetCityCountry

            return geocode_result, address
        except ValueError:
            return geocode_result
