import wikipedia

class Wikipedia:
    """Class used for the media wiki API REST requests"""

    def __init__(self, query):
        self.query = query

    def __repr__(self):
        '''Method to print the media wiki destination mess'''

        return self.query

    def get_request(self):
        '''method witch uses mediawiki client to request API'''
        place = ''
        wikipedia.set_lang("fr")
        try:
            place = wikipedia.summary(f"{self.query}", sentences=2) # two first sentences
        except wikipedia.exceptions.DisambiguationError as e:         
            try:
                place = wikipedia.summary(e.options[0], sentences=1)
            except wikipedia.exceptions.DisambiguationError as e:
                place = wikipedia.summary(e.options[1], sentences=1)       
            except IndexError:
                print("error")
                place = {"error": "no result"}
        return place





