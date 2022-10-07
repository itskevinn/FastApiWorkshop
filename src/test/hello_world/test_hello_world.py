import unittest

from src.core.hello_world.services.hello_world_service import welcome_to_fast_api


class HelloWorld(unittest.TestCase):
    def itShouldReturnHelloFastApi(self):
        self.assertEqual(welcome_to_fast_api, True)


if __name__ == '__main__':
    unittest.main()
