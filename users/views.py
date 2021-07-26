from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView

class UsersLoginView(LoginView):
	template_name = "users/login.html"



class UsersSignupView(TemplateView):
	template_name = "users/signup.html"
