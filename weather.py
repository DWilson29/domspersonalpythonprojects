# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 17:11:56 2021

@author: DomPC
"""

import requests
from plyer import notification

API_key = "23ce0ed48202989952b55471ae3fc7d7"
city_id = '5720727'


forecastURL = "https://api.openweathermap.org/data/2.5/onecall?lat=44.5646&lon=-123.262&units=imperial&exclude=current,minutely,hourly&appid=" + API_key
weather_Forecast = requests.get(forecastURL).json()

icon = "sunny.ico"
if weather_Forecast["daily"][0]["weather"][0]["main"] == "Rain" or weather_Forecast["daily"][0]["weather"][0]["main"] == "Drizzle":
    icon = "rain.ico"
elif weather_Forecast["daily"][0]["weather"][0]["main"] == "Clouds":
    icon = "cloudy.ico"
elif weather_Forecast["daily"][0]["weather"][0]["main"] == "Thunderstorm":
    icon = "lightning.ico"
elif weather_Forecast["daily"][0]["weather"][0]["main"] == "Snow":
    icon = "snow.ico"
info = "Sky is Clear"
if weather_Forecast["daily"][0]["clouds"] > 50:
    info = "Cloudy out there"
elif weather_Forecast["daily"][0]["pop"] > 0.5:
    info += " and rainy too!"
notification.notify(title="Weather Report", message=info,app_icon = icon)