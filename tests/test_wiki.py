from controler.wiki import Wikipedia as script
import wikipedia


def test_request_API_wikipedia(monkeypatch):

    results = "Dijon (prononcer [di.ʒɔ̃]) est une commune française"

    class MockResponse:
        
        def read(self):
            results_string = json.dumps(results) # creates a string from results
            results_bytes = results_string.encode()
            return results_bytes

    def moock_get_wiki_story(url):
        return MockResponse()

    monkeypatch.setattr('controler.wiki', moock_get_wiki_story)