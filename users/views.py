from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .forms import SignUpForm

class UsersLoginView(LoginView):
	template_name = "users/login.html"



class UsersSignupView(SuccessMessageMixin, CreateView):
	template_name = "users/signup.html"
	form_class = SignUpForm
	success_url = reverse_lazy("login")
	success_message = "Account created successfully."



class UsersLogoutView(LogoutView):
	next_page = "index"
