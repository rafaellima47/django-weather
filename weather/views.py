from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required

import requests as req

from .models import SavedCityModel


BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units={}"
API_KEY = settings.API_KEY



def get_user_location(request, cities):
	cities.append("Rio de Janeiro")
	return cities



def get_user_saved_cities(request, cities):
	for sc in SavedCityModel.objects.filter(user=request.user):
		cities.append(sc.city)
	return cities




def index(request):
	UNIT = "metric"
	context = {"cities": []}
	cities = []

	if request.method == "POST":
		cities.append(request.POST["city"])
		UNIT = request.POST["units"]

	cities = get_user_location(request, cities)
	if request.user.is_authenticated:
		cities = get_user_saved_cities(request, cities)

	for city in cities:
		try:
			resp = req.get(BASE_URL.format(city, API_KEY, UNIT))
			weather_data = resp.json()
		except:
			weather_data = None

		context["cities"].append(weather_data)

	context["unit"] = UNIT
	return render(request, "weather/index.html", context)



@login_required(login_url="login")
def save_city(request, city):
	sc = SavedCityModel()
	sc.city = city 
	sc.user = request.user 
	sc.save()
	return redirect("index")