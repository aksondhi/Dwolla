from utils import *

def main():

    city = None
    weather = None

    # Allowing input until a valid city is provided
    while True:

        city = getCity()

        try:

            # Using Open Weather Map to get weather data
            weather = getWeather(city)

            # Confirming the temperature is provided
            if "main" in weather and "temp" in weather.get("main"):
                print weather.get("name"), "weather:"
                print str(weather.get("main").get("temp")) + " degrees Fahrenheit"
            else:
                print "No weather data available."
            break

        except ValueError:
            print "Invalid city."

if __name__ == "__main__":
    main()