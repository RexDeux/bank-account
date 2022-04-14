from symtable import Symbol
from unicodedata import name
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import config
from twython import Twython, TwythonError
import datetime
import requests
import json


coin = Twython(config.api_key, config.api_secret, config.access_token, config.token_secret)
convert = 'USD'
headers = {'X-CMC_PRO_API_KEY': config.api_key }

base_url = 'https://pro-api.coinmarketcap.com'

global_url = base_url + '/v1/cryptocurrency/listings/latest'

request = requests.get(global_url, headers=headers)
results = request.json()

#print(json.dumps(results, sort_keys=True, indent=4))

data  = results['data']
for currency in data:
    rank = currency['cmc_rank']
    name = currency['name']
    symbol = currency['symbol']
    quote = currency['quote'][convert]
    price = quote['price']
    #rank = currency['id']
    print(str(rank) + ': ' + name + ' (' + symbol + ') '+ str(price) + ' ' + 'USD' '')
print(price)
print()