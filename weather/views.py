from django.shortcuts import render
from django.conf import settings
from django.views.generic import View

import requests as req


class IndexView(View):

	def get(self, request, *args, **kwargs):
		url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format("london", settings.API_KEY)
		response = req.get(url)
		weather_data = response.json()

		context = {"weather_data": weather_data}
		return render(requests, "weather/index.html", context)
