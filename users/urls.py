from django.urls import path

from . import views


urlpatterns = [
	path("login/", views.UsersLoginView.as_view(), name="login"),
	path("signup/", views.UsersSignupView.as_view(), name="signup"),
	path("logout/", views.UsersLogoutView.as_view(), name="logout"),
]