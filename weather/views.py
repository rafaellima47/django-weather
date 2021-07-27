from django.shortcuts import render, redirect
from django.conf import settings
from django.views.generic import View

import requests as req


class IndexView(View):
	url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units={}"
	appid = settings.API_KEY
	city = "orlando"
	unit = "metric"

	def get(self, request, *args, **kwargs):
		try:
			response = req.get(self.url.format(self.city, self.appid, self.unit))
			weather_data = response.json()
		except:
			weather_data = None

		context = {"weather_data": weather_data}
		return render(request, "weather/index.html", context)


	def post(self, request, *args, **kwargs):
		self.city = request.POST["city"]
		self.unit = request.POST["units"]
		return self.get(request)

