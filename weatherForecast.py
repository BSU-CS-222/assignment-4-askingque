import json
import ssl
from urllib.request import urlopen

def forecastURL():
    url = "https://api.weather.gov/points/40.1934,-85.3864"
    context = ssl._create_unverified_context()
    response = urlopen(url, context=context)
    urlData = json.loads(response.read())
    return urlData["properties"]["forecast"]

def weatherForTheWeek():
    context = ssl._create_unverified_context()
    response = urlopen(forecastURL(), context=context)
    weatherData = json.loads(response.read())
    for e in weatherData["properties"]["periods"]:
        print("Time: " + e["name"] + "\nTemperature: " + str(e["temperature"]) + "\nDetailed Forecast: "  + e["detailedForecast"])



weatherForTheWeek()