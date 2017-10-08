import requests
import json

baseURL = "http://api.openweathermap.org/data/2.5/weather"
apiKey = "09cc49e8cc6fd18f0e3455a455e7835d"


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
        raise ValueError(response.get("message", False) if "message" in response else ("Request Error. Status: " + str(request.status_code)))

    return response