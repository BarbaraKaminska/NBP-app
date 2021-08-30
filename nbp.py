import datetime
import requests


class ExchangeRate:
    def __init__(self, currency, code, ask_rate, bid_rate):
        self.currency = currency
        self.code = code
        self.ask_rate = ask_rate
        self.bid_rate = bid_rate

    def __str__(self):
        return f'< {self.currency} ({self.code}) \t{self.ask_rate}\t{self.bid_rate} >'


class ExchangeRateTable:
    def __init__(self, name, effective_date, rates=None):
        self.name = name
        self.effective_date = datetime.datetime.strptime(effective_date, '%Y-%m-%d')
        self._rates = rates if rates is not None else []
        # if instead of None one uses [] all instances would use the same list

    def __str__(self):
        return f'{self.name} - {self.effective_date}'

    def __getitem__(self, item):
        res = self.get_rate(item)
        if res is None:
            raise KeyError('Exchange error not found')
        return res

    def add_rate(self, rate):
        self._rates.append(rate)

    def get_rate(self, code):
        for rate in self._rates:
            if rate.code == code:
                return rate

    def rates(self):
        for rate in self._rates:
            yield rate

    def rate_by_code(self):
        return {curr.code: (curr.ask_rate, curr.bid_rate) for curr in self.rates()}


def get_exchange_rate_table(date, format='json'):
    url = f'http://api.nbp.pl/api/exchangerates/tables/C/{date}'
    params = {'format': format}
    resp = requests.get(url, params=params)
    try:
        resp.raise_for_status()
        if format == 'json':
            return _from_json(resp)
        else:
            return None
    except requests.exceptions.HTTPError:
        print('Connection error')


def _from_json(resp):
    resp_dict = resp.json()[0]
    rates = [ExchangeRate(rate['currency'], rate['code'], rate['ask'], rate['bid'])
             for rate in resp_dict['rates']]
    table = ExchangeRateTable(resp_dict['table'], resp_dict['effectiveDate'], rates)
    return table



