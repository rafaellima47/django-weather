from django.shortcuts import render

import requests as req

from .config import API_KEY

def index(requests):
	response = req.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format("london", API_KEY))
	weather_data = response.json()

	context = {"weather_data": weather_data}
	return render(requests, "weather/index.html", context)
