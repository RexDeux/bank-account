from requests import Request, Session
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import config
from twython import Twython, TwythonError


def CoinMarketCap(request):
    coin = Twython(config.api_key, config.api_secret, config.access_token, config.token_secret)
    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    
    id = '1'
    #ids = Id.objects.all()

    coin_data = []
    parameters = {
    'start':'1',
    'limit':'5000',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': config.api_key ,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    a = requests.get(url, headers=headers )
    #return(a.status_code)
    id_data = {
                'city': city.name,
                'temperature': a['main']['temp'],
                'temperature2': a['main']['feels_like'],
                'description': a['weather'][0]['description'],
                'icon': a['weather'][0]['icon'],
                'coordinate1': a['coord']['lon'],
                'coordinate2': a['coord']['lat'],
                'zone': a['sys']['country']

            }

    coin_data.append(id_data)