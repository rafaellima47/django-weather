from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required

import requests as req

from .models import SavedCityModel


BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units={}"
API_KEY = settings.API_KEY


def get_user_location(request):
	return "Rio de Janeiro"



def get_user_saved_cities(request):
	saved_cities = []
	for sc in SavedCityModel.objects.filter(user=request.user):
		saved_cities.append(sc.city)
	return saved_cities



def index(request):
	context = {"unit": "metric"}
	all_cities = []

	if request.method == "POST":
		context["search_city"] = request.POST["city"]
		context["unit"] = request.POST["units"]
		all_cities.append(context["search_city"])

	context["current_location"] = get_user_location(request)
	all_cities.append(context["current_location"])
	if request.user.is_authenticated:
		context["saved_cities"] = get_user_saved_cities(request)
		all_cities += context["saved_cities"]
		if context["current_location"] in context["saved_cities"]:
			all_cities.remove(context["current_location"])

	context["cities_data"] = []
	for city in all_cities:
		try:
			resp = req.get(BASE_URL.format(city, API_KEY, context["unit"]))
			weather_data = resp.json()
		except:
			weather_data = None

		context["cities_data"].append(weather_data)

	return render(request, "weather/index.html", context)



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