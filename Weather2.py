import re
import urllib.request as l

city = input("Enter city name: ")

url = "http://www.weather-forecast.com/locations/"+ city + "/forecasts/latest"

data = l.open(url).read()

data1 = data.decode("utf-8")