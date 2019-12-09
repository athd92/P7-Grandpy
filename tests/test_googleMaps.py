from controler.googleMaps import GoogleMaps



def test_request_API_googlemaps_mock(monkeypatch):

    results = [{"city": "Paris", "country": 'France'}] 

    class MockResponse:
        
        def read(self):
            results_string = json.dumps(results) # creates a string from results
            results_bytes = results_string.encode()
            return results_bytes

    def moock_get_geocode_googlemaps(url):
        return MockResponse()

    monkeypatch.setattr('controler.googleMaps', moock_get_geocode_googlemaps)