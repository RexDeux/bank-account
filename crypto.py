from requests import Request, Session
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import config
from twython import Twython, TwythonError


def CoinMarketCap(request):
    coin = Twython(config.api_key, config.api_secret, config.access_token, config.token_secret)
    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    
    #id = '1'
    #ids = Id.objects.all()
    coin_data = []
    ids = id.objects.all()

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

    for id in ids:
        
        a = requests.get(url, headers=headers )
        #return(a.status_code)
        id_data = {
                    'id': id.name,
                    'rank': a['main']['rank'],
                    'symbol': a['main']['symbol'],
                    'slug': a['weather'][0]['slug'],
                    'is_active': a['weather'][0]['is_active'],
                    'first_historical_date': a['first_historical_date'],
                    'last_historical_date': a['lat'],
                    }

        coin_data.append(id_data)
        
    print(coin_data)