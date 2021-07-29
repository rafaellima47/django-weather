from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.generic import View

import requests as req

from .models import SavedCityModel


class IndexView(View):

	def __init__(self, **kwargs):
		super(IndexView, **kwargs).__init__()
		self.context = {"cities": []}
		self.unit = "metric"



	def get(self, request):
		self.get_user_location(request)
		if request.user.is_authenticated:
			self.get_user_saved_cities(request)

		self.context["unit"] = self.unit
		return render(request, "weather/index.html", self.context)



	def post(self,request):
		self.context["cities"].append(self.get_weather_data(request.POST["city"]))
		self.unit = request.POST["units"]
		return self.get(request)



	def get_user_location(self, request):
		self.context["cities"].append(self.get_weather_data("Rio de Janeiro"))
		self.context["current_location"] = "Rio de Janeiro"



	def get_user_saved_cities(self, request):
		self.context["saved"] = []
		for sc in SavedCityModel.objects.filter(user=request.user):
			self.context["cities"].append(self.get_weather_data(sc.city))
			self.context["saved"].append(sc.city)



	def get_weather_data(self, city):
		try:
			resp = req.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units={}".format(city, settings.API_KEY, self.unit))
			weather_data = resp.json()
		except:
			weather_data = None
		return weather_data



@login_required(login_url="login")
def save_city(request, city):
	sc = SavedCityModel()
	sc.city = city 
	sc.user = request.user 
	sc.save()
	return redirect("index")


@login_required(login_url="login")
def unsave_city(request, city):
	sc = SavedCityModel.objects.filter(user=request.user)
	sc.filter(city=city).delete()
	return redirect("index")