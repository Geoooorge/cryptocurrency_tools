import requests
import pickle 
from twilio.rest import Client
from api_keys import *

client = Client(ACCOUNT_SID, AUTH_TOKEN)

r = requests.get('https://api.binance.com/api/v3/ticker/bookTicker')
data = r.json()

def send_message():
    client.messages.create(
        to=TO_NUMBER, 
        from_=FROM_NUMBER,
        body=coin_list)

currency_pairs = []
for item in data:
    currency_pairs.append(item['symbol'])

try:
    with open('save.p', 'rb') as f:
        current_coins = pickle.load(f)
except (OSError, IOError) as e:
    with open('save.p', 'wb') as f:
        pickle.dump(currency_pairs, f, protocol=pickle.HIGHEST_PROTOCOL)
    print('Initial coin pair list has been populated')
    quit()

difference = set(currency_pairs) - set(current_coins)

if difference != set():
    coin_list = 'Binance added: '
    for coin in difference:
        coin_list += coin + ' '
    print(coin_list)
    send_message()

    with open('save.p', 'wb') as f:
        pickle.dump(currency_pairs, f, protocol=pickle.HIGHEST_PROTOCOL)