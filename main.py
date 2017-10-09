__author__ = "Arun Sondhi"

from utils import *


# The main method functions as the user interface to retrieve user input and then temperature.
# If the user fails to input a valid city, they will continue to be prompted until a valid city is provided.
def main():
    # Allowing input until a valid city is provided
    while True:

        city = getCity()

        try:

            # Using Open Weather Map to get weather data
            weather = getWeather(city)

            # Confirming the temperature is provided
            if "main" in weather and "temp" in weather.get("main"):
                print weather.get("name"), "weather:"
                print str(round(weather.get("main").get("temp"), 2)) + " degrees Fahrenheit"
                break
            else:
                print "No weather data available."

        except ValueError:
            print "Invalid city."


if __name__ == "__main__":
    main()
