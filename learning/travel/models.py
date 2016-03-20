import datetime

# Create your models here.
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone


class User(models.Model):
	user_name = models.CharField(max_length=20)

	def __str__(self):
        	return self.user_name

class Itinerary(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	source_city=models.CharField(max_length=50)
	dest_city=models.CharField(max_length=50)
	start_date=models.DateTimeField()
	num_days=models.IntegerField(default=0)
	
	def __str__(self):
        	return self.user.user_name + ":" + self.source_city + " to " + self.dest_city 

	def travelling_soon(self):
		return self.start_date >= timezone.now() + datetime.timedelta(days=20)
