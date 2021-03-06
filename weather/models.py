from django.db import models
from django.contrib.auth.models import User

class SavedCityModel(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	city = models.TextField()
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.city

