from serpapi import GoogleSearch
from requests import Request, Session
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import config
from twython import Twython, TwythonError

class Twitter():
    coin = Twython(config.secret_api_key, config.api_secret, config.access_token, config.token_secret)
    a = 'https://serpapi.com/search.json?q=Naval+twitter&location=Austin%2CTexas%2CUnited+States&hl=en&gl=us&api_key='
    url = a + config.secret_api_key
    params = {
    "q": "Naval twitter",
    "location": "Austin,Texas,United States",
    "hl": "en",
    "gl": "us",
    "api_key": "ec7d0ec40feb0712e9cfd982f0c44d402ea2dc34f53df99fb2d0889fbf1d4e4a"
    }
    json_data = requests.get(url).json
    #json_status = json_data('source')
    #print('API Status: ' + json_status + '\n')
    search = GoogleSearch(params)
    results = search.get_dict()

    twitter = results['twitter_results']
    tweets = results['twitter_results']['tweets']
    #print(twitter_results)
    print(tweets)
    #def tweet():
        #json_data = Twitter.json_data
        #json_status = Twitter.json_data['source']
        #return(json_data)