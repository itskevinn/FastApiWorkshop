import unittest

from core.fibonacci.services.fibonacci_service import get_value_due_to_position


class MyTestCase(unittest.TestCase):
    def testItShouldReturnTheCorrectNumberDueToPosition(self):
        self.assertEqual(get_value_due_to_position(2), 2)


if __name__ == '__main__':
    unittest.main()
