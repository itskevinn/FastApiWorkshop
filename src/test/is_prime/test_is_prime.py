import unittest

from src.core.prime_numbers.services.prime_number_service import calculate_is_prime_number


class MyTestCase(unittest.TestCase):
    def testShouldReturnTrueIsPrimeNumber(self):
        self.assertEqual(calculate_is_prime_number(5), True)

    def testShouldReturnFalseIsNotAPrimeNumber(self):
        self.assertEqual(calculate_is_prime_number(1), False)

    def testShouldReturnFalseIsNotsPrimeNumber(self):
        self.assertEqual(calculate_is_prime_number(0), False)

    def testShouldReturnFalseIsNotIsAPrimeNumber(self):
        self.assertEqual(calculate_is_prime_number(4), False)


if __name__ == '__main__':
    unittest.main()
