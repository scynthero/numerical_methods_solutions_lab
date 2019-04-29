import requests

response_bitbay = requests.get("https://bitbay.net/API/Public/BTCPLN/ticker.json")
response_bitmarket = requests.get("https://www.bitmarket.pl/json/BTCPLN/ticker.json")
data_bitbay = response_bitbay.json()
data_bitmarket = response_bitmarket.json()
if data_bitbay['bid'] > data_bitmarket['bid']:
    best_bid = data_bitbay['bid']
    print("Currently bitbay is better for selling")
elif data_bitbay['bid'] < data_bitmarket['bid']:
    best_bid = data_bitmarket['bid']
    print("Currently bitmarket is better for selling")
else:
    best_bid = data_bitbay['bid']
    print("Currently sell price is equal")

if data_bitbay['ask'] > data_bitmarket['ask']:
    best_ask = data_bitbay['ask']
    print("whilst bitmarket is better for buying")
elif data_bitbay['ask'] < data_bitmarket['ask']:
    best_ask = data_bitmarket['ask']
    print("whilst bitbay is better for buying")
else:
    best_ask = data_bitbay['ask']
    print("whilst buy price is equal")
print('bid:', best_bid, 'ask:', best_ask)
