import serpapi
from serpapi import GoogleSearch

class Twitter():
    def index(request):
        url = 'https://serpapi.com/search.json?q=Naval+twitter&location=Austin%2CTexas%2CUnited+States&hl=en&gl=us&api_key=ec7d0ec40feb0712e9cfd982f0c44d402ea2dc34f53df99fb2d0889fbf1d4e4a'
        params = {
        "q": "Naval twitter",
        "location": "Austin,Texas,United States",
        "hl": "en",
        "gl": "us",
        "api_key": "secret_api_key"
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        twitter_results = results['twitter_results']
        return(twitter_results)