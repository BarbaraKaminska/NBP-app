import nbp

# if one imports this way: 'from nbp import ExchangeRate' prefix 'nbp.' is not needed
from functools import wraps


def add_separators(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("=" * 50)
        func(*args, **kwargs)
        print("=" * 50)

    return wrapper


@add_separators
def print_header(rate_table):
    print(f"Table: {rate_table.name}\tDate: " f"{rate_table.effective_date.date()}")


if __name__ == "__main__":
    usd = nbp.ExchangeRate("Dolar amerykanski", "USD", 4.1, 4.0)
    eur = nbp.ExchangeRate("Euro", "EUR", 4.6, 4.5)
    table = nbp.ExchangeRateTable("exchange", "2021-08-19")
    table.add_rate(usd)
    table.add_rate(eur)

    """    
    for rate in table.rates:
        print(rate)
    try:
        print(f"{table['PLN']}")
    except KeyError as e:
        print('Currency not found')
        print(e)
    """

    new_table = nbp.get_exchange_rate_table("2021-08-27", "xml")
    print_header(new_table)
    for rate in new_table.rates():
        print(rate)
