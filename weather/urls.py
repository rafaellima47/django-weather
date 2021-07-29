from django.urls import path

from . import views

urlpatterns = [
	path("", views.IndexView.as_view(), name="index"),
	path("save_city/<str:city>", views.save_city, name="save_city"),
	path("unsave_city/<str:city>", views.unsave_city, name="unsave_city"),
]