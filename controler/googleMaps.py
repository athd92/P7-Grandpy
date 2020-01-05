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

        res = gmaps.geocode(self.query)
        if res == []:
            self.query = [self.query, 'france']
            res = gmaps.geocode(self.query)
        try:
            streetNumber = res[0]['address_components'][0]['short_name']
            streetName = res[0]['address_components'][1]['long_name']
            streetCity = res[0]['address_components'][2]['long_name']
            streetComplement = res[0]['address_components'][3]['long_name']
            streetCityName = res[0]['address_components'][4]['long_name']
            streetCitySecondName = res[0]['address_components'][5]['long_name']
            streetCityCountry = res[0]['address_components'][6]['long_name']

            address = streetNumber + '\
                ' + streetName + ' \
                ' + streetCity + ' \
                ' + streetComplement + ' \
                ' + streetCityName + ' \
                ' + streetCitySecondName + ' \
                ' + streetCityCountry

            return res, address
        except ValueError:
            return res
