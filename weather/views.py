from django.shortcuts import render, redirect
from django.conf import settings
from django.views.generic import View
from django.contrib.auth.decorators import login_required

from .models import SavedCityModel

import requests as req


class IndexView(View):
	url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units={}"
	appid = settings.API_KEY
	city = "Rio de Janeiro"
	unit = "metric"

	def get(self, request, *args, **kwargs):
		try:
			response = req.get(self.url.format(self.city, self.appid, self.unit))
			weather_data = response.json()
		except:
			weather_data = None

		context = {"weather_data": weather_data, "unit": self.unit}
		return render(request, "weather/index.html", context)


	def post(self, request, *args, **kwargs):
		self.city = request.POST["city"]
		self.unit = request.POST["units"]
		return self.get(request)



@login_required(login_url="login")
def save_city(request, city):
	sc = SavedCityModel()
	sc.city = city 
	sc.user = request.user 
	sc.save()
	return redirect("index")


