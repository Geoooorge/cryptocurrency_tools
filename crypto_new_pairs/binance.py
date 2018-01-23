import requests
import pickle

r = requests.get('https://api.binance.com/api/v3/ticker/bookTicker')
data = r.json()

currency_pairs = []
for item in data:
    currency_pairs.append(item['symbol'])
# currency_pairs.remove('123456')
# initial_save = pickle.dump(currency_pairs, open("save.p", "wb"))
current_coins = pickle.load(open("save.p", "rb"))

difference = set(currency_pairs) - set(current_coins)

if difference != set():
    for u in difference:
        print(u)



