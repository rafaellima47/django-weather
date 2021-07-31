from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login

from .forms import SignUpForm

class UsersLoginView(LoginView):
	template_name = "users/login.html"



class UsersSignupView(CreateView):
	template_name = "users/signup.html"
	form_class = SignUpForm
	success_url = reverse_lazy("index")

	def form_valid(self, form):
		valid = super(UsersSignupView, self).form_valid(form)
		username, password = form.cleaned_data.get("username"), form.cleaned_data.get("password1")
		user = authenticate(username=username, password=password)
		login(self.request, user)
		return valid

	


class UsersLogoutView(LogoutView):
	next_page = "index"
