from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView

from .forms import SignUpForm

class UsersLoginView(LoginView):
	template_name = "users/login.html"



class UsersSignupView(CreateView):
	template_name = "users/signup.html"
	form_class = SignUpForm
