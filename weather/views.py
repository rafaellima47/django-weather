from django.shortcuts import render, redirect
from django.conf import settings
from django.views.generic import View

import requests as req


class IndexView(View):

	def get(self, request, *args, **kwargs):
		url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format("london", settings.API_KEY)
		try:
			response = req.get(url)
			weather_data = response.json()
		except:
			weather_data = None

		context = {"weather_data": weather_data}
		return render(request, "weather/index.html", context)


	def post(self, request, *args, **kwargs):
		return redirect("index")

