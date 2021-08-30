import unittest
from nbp import ExchangeRate


class NBPTest(unittest.TestCase):
    def setUp(self):
        self.e = ExchangeRate('dolar amerykanski', 'USD', 4.0029, 3.9225)

    def test_exchange_rate_creation(self):
        self.assertEqual(self.e.code, 'USD')
        self.assertEqual(self.e.currency, 'dolar amerykanski')
        self.assertAlmostEqual(self.e.bid_rate, 3.9225)
        self.assertAlmostEqual(self.e.ask_rate, 4.0029)


class NBPTestExchangeRateTable(unittest.TestCase):
    def setUp(self):
        # here prepare set up before all tests (in case eg. some tests modify data)
        pass


if __name__ == '__main__':
    unittest.main()
