# This file contains contains tests for the utils.py methods.
__author__ = "Arun Sondhi"

import unittest
import mock
import httpretty
import __builtin__
from utils import *


def test_raw_input():
    return raw_input()


class TestUtils(unittest.TestCase):
    @mock.patch.object(__builtin__, 'raw_input')
    def test_getCity(self, mock_raw_input):
        # Testing input handler
        mock_raw_input.return_value = "Des Moines, IA"
        self.assertEqual(getCity(), "Des Moines, IA")

    @httpretty.activate
    def test_getWeather_basicInput(self):
        # Testing basic input with minimal data
        httpretty.register_uri(httpretty.GET, "http://api.openweathermap.org/data/2.5/weather",
                               body=json.dumps({
                                   "main": {
                                       "temp": 46.99,
                                       "pressure": 1022,
                                       "humidity": 87,
                                       "temp_min": 46.4,
                                       "temp_max": 48.2
                                   },
                                   "id": 4853828,
                                   "name": "Des Moines",
                                   "cod": 200
                               }))

        weather = getWeather("Des Moines, IA")
        self.assertTrue("cod" in weather)
        self.assertEqual(weather.get("cod"), 200)
        self.assertTrue("name" in weather)
        self.assertEqual(weather.get("name"), "Des Moines")
        self.assertTrue("id" in weather)
        self.assertEqual(weather.get("id"), 4853828)

    @httpretty.activate
    def test_getWeather_invalidInput(self):
        # Testing invalid input
        httpretty.register_uri(httpretty.GET, "http://api.openweathermap.org/data/2.5/weather",
                               body=json.dumps({
                                   "cod": "404",
                                   "message": "city not found"
                               }))
        with self.assertRaises(ValueError):
            weather = getWeather("abcdefg")


if __name__ == '__main__':
    unittest.main()
