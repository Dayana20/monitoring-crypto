import db.db_connect as dbc
from coinmarketcapapi import CoinMarketCapAPI

# from config import API_KEY
# https://pypi.org/project/python-coinmarketcap/

API_KEY = ''
COINS_COLLECT = 'coins'
COIN_DB = 'coindb'
ID = 'id'
NAME = 'name'
SYMBOL = 'symbol'
PRICE = 'price'
TEST_COIN = 'Bitcoin'
REQUIRED_FIELDS = [ID, NAME, SYMBOL, PRICE]

# database will use
coin_type = {'Bitcoin': {'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC',
             'price': 20237.84301693455}, 'Litecoin': {'id': 2,
             'name': 'Litecoin', 'symbol': 'LTC', 'price': 62.885530866205976}}


# should save to a database in the future
def coinapi_setup():
    cmc = CoinMarketCapAPI(API_KEY)
    r = cmc.cryptocurrency_map()
    # only using first 10 coins for now
    for line in r.data[2:10]:
        # metaData = cmc.cryptocurrency_info(id = line['id']) - INCLUDES
        # DESCRIPTION metaData.data['description'], metaData.data['logo']
        # print(metaData.data)
        quote = cmc.cryptocurrency_quotes_latest(symbol=line['symbol'])
        price = quote.data[line['symbol']]['quote']['USD']['price']
        # coin_type[line['name']] = {ID: line['id'], NAME: line['name'],
        #                            SYMBOL: line['symbol'], PRICE: price}
        return save_coin(line['name'], {ID: line['id'], NAME: line['name'],
                                        SYMBOL: line['symbol'], PRICE: price})


def save_coin(name, dets):
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')
    if not isinstance(dets, dict):
        raise TypeError(f'Wrong type for coin details: {type(dets)=}')
    if coin_exists(name):
        raise ValueError("Coin already exists!")
    coin_type[name] = dets
    dbc.connect_db()
    dbc.insert_one(COINS_COLLECT, coin_type[name], COIN_DB)
    return True


def remove_coin(name):
    dbc.connect_db()
    if not coin_exists(name):
        raise TypeError(f'Coin: {type(name)=} does not exist in db.')
    dbc.remove_one(COINS_COLLECT, coin_type[name], COIN_DB)
    del coin_type[name]
    return True


def coin_exists(name):
    return name in coin_type


def coin_details(name):
    return coin_type.get(name, None)


def get_coins():
    return list(coin_type.keys())


def get_coin_dict():
    '''
    FOR MENU
    '''
    return coin_type


def count_coins():
    return len(coin_type.keys())


def coin_price(name):
    return coin_type[name]['price']


def get_coin_ticker(name):
    return coin_type[name]['symbol']


def remodel_coin_ticker(name, remodel_symbol):
    coin_type[name]['symbol'] = remodel_symbol
    return True


def get_all_coin_tickers():
    tickers = []
    for coin in coin_type.keys():
        tickers.append(coin_type[coin]['symbol'])
    return tickers


def change_coin_price(name, new_price):
    coin_type[name]['price'] = new_price
    return coin_type[name]['price']


def main():
    coinapi_setup()
    print(coin_type)
