# This file contains utility functions for city input via the user and retrieving weather data from Open Weather Map.
__author__ = "Arun Sondhi"

import requests
import json
import os

baseURL = "http://api.openweathermap.org/data/2.5/weather"

# Retrieving api key from environment
try:
    apiKey = os.environ['OPENWEATHERMAPKEY']
except:
    raise ValueError("OPENWEATHERMAPKEY is a required environment variable")


def getCity():
    """
    Retrieves city input from user.
    :return: Returns user input.
    """
    city = raw_input("Where are you? ")
    return city


def getWeather(city):
    """
    Retrieves the given city's weather data. Raises a value error if the query fails to return a valid result.
    :param city: A city to be passed to Open Weather Map Query (string).
    :return: Returns the given city's weather data as a dictionary.
    """
    request = requests.get(baseURL + "?q=" + city + "&units=imperial" + "&APPID=" + apiKey)
    response = json.loads(request.content)

    if response.get('cod') != 200:
        raise ValueError(response.get("message", False) if "message" in response else (
            "Request Error. Status: " + str(request.status_code)))

    return response
