import dataset
import requests
import random
import os

#define a person
class Person:
    def __init__(self,id,table):
        user = table.find_one(id=id)
        self.name = user['first_name']
        self.balancebtc = user['balancebtc']
        self.balancepln = user['balancepln']
#populate database function
def populate(table):
    for i in range(100):
        user = requests.get('https://randomuser.me/api/').json()
        table.insert(dict(username=user['results'][0]['login']['username'],
                          first_name=user['results'][0]['name']['first'],
                          surname=user['results'][0]['name']['last'],
                          balancebtc=random.uniform(1, 10),
                          balancepln=random.uniform(1, 300000)))
#transaction function
def transaction():
    '''
    rand1 = random.randint(1,101)
    rand2 = random.randint(1, 101)
    user1 = table.find_one(id=rand1)
    user2 = table.find_one(id=rand2)
    user1_btc_balance = random.uniform(1,user1['balancebtc'])
    user1_pln_balance = random.uniform(1, user1['balancepln'])
    user2_pln_balance = random.uniform(1,user2['balancepln'])
    btc_sell_price = user1_btc_balance * data_bitmarket['ask']
    if user2_pln_balance > btc_sell_price:
        user2_pln_balance = user2_pln_balance - btc_sell_price
        user2_btc_balance =
    #user 1 tries to sell btc
    #user 2 tries to buy btc
    '''
    return 0
#fetch btc data
data_bitmarket = requests.get("https://www.bitmarket.pl/json/BTCPLN/ticker.json").json()
#connect to database
db = dataset.connect('sqlite:///ex2.db')
table = db['user']
#check if database file exists, if no use populate function to fetch data from api
exists = os.path.isfile('ex2.db')
if not exists:
    print("populating database with random users")
    populate(table)
#test
transaction()
person = Person(3,table)
print(person.balancepln)