import unittest

from src.core.fibonacci.services.fibonacci_service import get_value_due_to_position


class FibonacciTest(unittest.TestCase):
    def testItShouldReturnTheCorrectNumberDueToPosition(self):
        self.assertEqual(get_value_due_to_position(1), 0)

    def testItShouldReturn5InThePosition5(self):
        self.assertEqual(get_value_due_to_position(5), 3)

    def testItShouldReturn0IfNumberIsLessThan1(self):
        self.assertEqual(get_value_due_to_position(-1), 0)


if __name__ == '__main__':
    unittest.main()
