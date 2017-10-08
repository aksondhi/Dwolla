import unittest
import mock
import __builtin__
from utils import *
from main import main

def test_raw_input():
    return raw_input()

class TestUtils(unittest.TestCase):

    @mock.patch.object(__builtin__, 'raw_input')
    def test_getCity(self, mock_raw_input):
        # Testing input handler
        mock_raw_input.return_value = "Des Moines, IA"
        self.assertEqual(getCity(), "Des Moines, IA")

    def test_getWeather_basicInput(self):
        # Testing basic input
        weather = getWeather("Des Moines, IA")
        self.assertTrue("cod" in weather)
        self.assertEqual(weather.get("cod"), 200)
        self.assertTrue("name" in weather)
        self.assertEqual(weather.get("name"), "Des Moines")
        self.assertTrue("id" in weather)
        self.assertEqual(weather.get("id"), 4853828)

        # Confirming response contains expected weather data
        self.assertTrue("main" in weather)
        self.assertTrue("temp" in weather.get("main"))

    def test_getWeather_invlidInput(self):
        # Testing invalid input
        with self.assertRaises(ValueError):
            weather = getWeather("abcdefg")

if __name__ == '__main__':
    unittest.main()