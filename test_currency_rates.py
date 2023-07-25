import unittest
from currency_rates import currency_rates


class TestCurrencyRates(unittest.TestCase):

    def test_valid_currency(self):
        result = currency_rates('USD', '2022-10-08')
        self.assertIsNotNone(result)
        self.assertEqual(result['code'], 'USD')

    def test_invalid_currency(self):
        result = currency_rates('ZZZ', '2022-10-08')
        self.assertIsNone(result)

    def test_invalid_date(self):
        with self.assertRaises(ValueError):
            currency_rates("USD", "2022-13-40")


if __name__ == '__main__':
    unittest.main()
