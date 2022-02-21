from serpapi import GoogleSearch
from requests import Request, Session
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import config
from twython import Twython, TwythonError

def Twitter(request):
    coin = Twython(config.secret_api_key, config.secret_api_secret, config.secret_access_token, config.secret_token_secret)
    url = 'https://serpapi.com/search.json?q=Naval+twitter&location=Austin%2CTexas%2CUnited+States&hl=en&gl=us&api_key={secret_api_key}'
    params = {
    "q": "Naval twitter",
    "location": "Austin,Texas,United States",
    "hl": "en",
    "gl": "us",
    "secret_api_key": config.secret_api_key,
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    twitter_results = results['twitter_results']