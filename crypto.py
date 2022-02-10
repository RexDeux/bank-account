from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import config
from twython import Twython, TwythonError

def CoinMarketCap():

    coin = Twython(config.api_key, config.api_secret, config.access_token, config.token_secret)
    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
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
