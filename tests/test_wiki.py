from controler.wiki import Wikipedia as script
import wikipedia


def test_request_API_wikipedia(monkeypatch):

    results = "Lyon (prononcé /ljɔ̃/ ou /liɔ̃/ ) est une commune\
         française située dans le quart sud-est de la France au\
         confluent du Rhône et de la Saône. Siège du conseil de\
         la métropole de Lyon, elle est le chef-lieu de\
         l'arrondissement de Lyon, de la circonscription\
         départementale du Rhône et de la région Auvergne-Rhône-Alpes.\
         Le gentilé est Lyonnais. Lyon a une situation de carrefour\
         géographique du pays, au nord du couloir naturel de la\
         vallée du Rhône (qui s'étend de Lyon à Marseille)."

    class MockResponse:
        
        def read(self):
            results_string = json.dumps(results) # creates a string from results
            results_bytes = results_string.encode()
            return results_bytes

    def moock_get_wiki_story(url):
        
        response = MockResponse(url)
        result = response.moock_get_wiki_story()
        assert result ==  "Lyon (prononcé /ljɔ̃/ ou /liɔ̃/ ) est une commune\
         française située dans le quart sud-est de la France au\
         confluent du Rhône et de la Saône. Siège du conseil de\
         la métropole de Lyon, elle est le chef-lieu de\
         l'arrondissement de Lyon, de la circonscription\
         départementale du Rhône et de la région Auvergne-Rhône-Alpes.\
         Le gentilé est Lyonnais. Lyon a une situation de carrefour\
         géographique du pays, au nord du couloir naturel de la\
         vallée du Rhône (qui s'étend de Lyon à Marseille)."

    monkeypatch.setattr('controler.wiki', moock_get_wiki_story)
