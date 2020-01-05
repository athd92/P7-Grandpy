from controler.googleMaps import GoogleMaps
import json


def test_request_API_googlemaps_mock(monkeypatch):
    'Test function of the API Google maps'

    results = [{'address_components': [{'long_name': 'Lyon',
                'short_name': 'Lyon', 'types': ['locality', 'political']},
               {'long_name': 'Rhône', 'short_name': 'Rhône',
               'types': ['administrative_area_level_2', 'political']},
               {'long_name': 'Auvergne-Rhône-Alpes', 'short_name':
                'Auvergne-Rhône-Alpes',
                'types': ['administrative_area_level_1', 'political']},
               {'long_name': 'France', 'short_name': 'FR', 'types': ['country',
                'political']}], 'formatted_address': 'Lyon, France',
                'geometry':
                {'bounds': {'northeast': {'lat': 45.808425, 'lng': 4.898393},
                 'southwest': {'lat': 45.707486, 'lng': 4.7718489}},
                 'location': {'lat': 45.764043,  'lng': 4.835659},
                 'location_type': 'APPROXIMATE', 'viewport':
                 {'northeast': {'lat': 45.808425, 'lng': 4.898393},
                  'southwest': {'lat': 45.707486, 'lng': 4.7718489}}},
                'place_id': 'ChIJl4foalHq9EcR8CG75CqrCAQ',
                'types': ['locality', 'political']}]

    class MockResponse:
        '''Class defined to to the googlemaps requests'''

        def read(self):
            results_string = json.dumps(results)  # creates a string
            results_bytes = results_string.encode()
            return results_bytes

    def moock_get_geocode_googlemaps(url):
        '''Method used to mock the API return of googlemaps'''

        response = MockResponse(url)
        result = response.moock_get_geocode_googlemaps()
        assert result[0]['address_components'][0]['long_name'] == 'lyon'
        assert result[0]['geometry']['location']['lat'] == 45.764043
        assert result[0]['geometry']['location']['lng'] == 4.835659

        ask = "jkbsmezibgzelibgezmigb"
        response = MockResponse(ask)
        result = response.moock_get_geocode_googlemaps()
        assert result == {"data": "no result", 'localisation':
                          'no localisation possible'}

    monkeypatch.setattr('controler.googleMaps', moock_get_geocode_googlemaps)
