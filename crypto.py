from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import config
from twython import Twython, TwythonError
import datetime
import requests
import json


coin = Twython(config.api_key, config.api_secret, config.access_token, config.token_secret)

headers = {'X-CMC_PRO_API_KEY': config.api_key }

base_url = 'https://pro-api.coinmarketcap.com'

global_url = base_url + '/v1/cryptocurrency/listings/latest'

request = requests.get(global_url, headers=headers)
results = request.json()

#print(json.dumps(results, sort_keys=True, indent=4))

data  = results['data']

btc = data['name']


print(btc)