from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def CoinMarketCap():
    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
    'start':'1',
    'limit':'5000',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '3b42e93c-5fa0-41af-bea2-cd3d355074cc',
    }

    session = Session()
    session.headers.update(headers)

    try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
