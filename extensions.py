import json
import requests
from cfg import keys
class ConvertionException(Exception):
    pass
class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):




        if quote == base:
            raise ConvertionException('нельзя переводить в ту же валюту')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}. \n Проверьте правильность написания.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}. \n Проверьте правильность написания.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}. \n введите верное число.' )

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base