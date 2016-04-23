import datetime

# Create your models here.
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone


class User(models.Model):
    user_name = models.CharField(max_length=20)

    def __str__(self):
        return self.user_name

class CityItinerary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # An itinerary can only have one user. A user can have many itineraries,
    country = models.CharField(max_length=50)
    source_city = models.CharField(max_length=50)
    dest_city = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    num_days = models.IntegerField(default=0)

class City(models.Model):
    city=models.CharField(max_length=50)

class Place(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE) # A place can belong to only one city. A city can have many places
    type = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

class Activities(models.Model):
    type=models.CharField(max_length=20)

class Itinerary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source_city = models.CharField(max_length=50)
    dest_city = models.CharField(max_length=50)
    start_date = models.DateTimeField()
    num_days = models.IntegerField(default=0)

    def __str__(self):
        return self.user.user_name + ":" + self.source_city + " to " + self.dest_city

    def travelling_soon(self):
        return self.start_date >= timezone.now() + datetime.timedelta(days=20)




