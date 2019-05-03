import dataset
import requests
import random
import os
import time


# define a class Person
class Person:
    # constructor
    def __init__(self, id, table):
        user = table.find_one(id=id)
        self.id = user['id']
        self.username = user['username']
        self.name = user['first_name']
        self.surname = user['surname']
        self.balancebtc = user['balancebtc']
        self.balancepln = user['balancepln']

    # update database
    def update(self):
        table.update(dict(id=self.id, balancepln=self.balancepln, balancebtc=self.balancebtc), ['id'])


# populate database function
def populate(table):
    for i in range(100):
        user = requests.get('https://randomuser.me/api/').json()
        table.insert(dict(username=user['results'][0]['login']['username'],
                          first_name=user['results'][0]['name']['first'],
                          surname=user['results'][0]['name']['last'],
                          balancebtc=round(random.uniform(1, 10), 3),
                          balancepln=round(random.uniform(1, 300000), 3)))


# transaction function
def transaction():
    # fetch btc to pln data
    data_bitmarket = requests.get("https://www.bitmarket.pl/json/BTCPLN/ticker.json").json()
    # get 2 random users from database
    user1 = Person(random.randint(1, 100), table)
    user2 = Person(random.randint(1, 100), table)
    # get random amount of btc that user1 wants to trade
    user1_sell_amount = round(random.uniform(0.0001, user1.balancebtc), 3)
    # count sell price using fetched data
    btc_sell_price = round(user1_sell_amount * data_bitmarket['ask'], 3)
    # check if user2 has enough pln to buy btc
    if user2.balancepln < round(0.0001 * data_bitmarket['ask'], 3):
        return 0
    # if user1 wants to trade to mutch btc, randomize btc trade amount again
    # (don't want to simulate pln buy out situation from user2)
    while (user2.balancepln < btc_sell_price):
        user1_sell_amount = round(random.uniform(0.0001, user1.balancebtc), 3)
        btc_sell_price = round(user1_sell_amount * data_bitmarket['ask'], 3)
    # count account balances
    if user2.balancepln > btc_sell_price:
        user2.balancepln -= btc_sell_price
        user2.balancebtc += user1_sell_amount
        user1.balancepln += btc_sell_price
        user1.balancebtc -= user1_sell_amount
        # dirty fix due to rounding cousing negative numbers to appear
        if user1.balancepln < 0 or user1.balancebtc < 0 or user2.balancepln < 0 or user2.balancebtc < 0:
            return 1
        else:
            # update database and return data
            user1.update()
            user2.update()
            return user1.username, user1_sell_amount, user2.username, btc_sell_price


# connect to database
db = dataset.connect('sqlite:///ex2.db')
table = db['user']

# check if database file exists, if not, use populate function to fetch data from api
if not os.path.isfile('ex2.db'):
    print("populating database with random users")
    populate(table)

# transaction
while 1:
    start = time.time()
    for i in range(100):
        result = transaction()
        if result is 0:
            print("not enough money for transaction")
        elif result is 1:
            print("negative balance")
        else:
            print("{} exchanged {} BTC with {} for {} PLN".format(result[0], result[1], result[2], result[3]))
    end = time.time()
    print("\n elapsed time for 100 transactions: {} seconds \n".format(round(end - start), 2))
