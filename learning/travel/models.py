import datetime

# Create your models here.
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

class Activities(models.Model):
    type = models.CharField(max_length=20)

class User(models.Model):
    user_name = models.CharField(max_length=20)
    activities=models.ManyToManyField(Activities) # A user can have many activities and an activity can be part of many users. See https://docs.djangoproject.com/ja/1.9/topics/db/models/#many-to-many-relationships

    def __str__(self):
        return self.user_name

class Country(models.Model):
    country = models.CharField(max_length=50, default = "default")

class City(models.Model):
    city = models.CharField(max_length=50)
    country = models.ForeignKey(Country,
                                on_delete=models.CASCADE)  # A city can belong to only one country. A country can have many cities.

class Place(models.Model):
    city = models.ForeignKey(City,
                             on_delete=models.CASCADE)  # A place can belong to only one city. A city can have many places
    type = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

class UserItinerary(models.Model): # Represents a list of cities that a user wants to travel to.
    user = models.ForeignKey(User, on_delete=models.CASCADE) # An itinerary can only have one user. A user can have many itineraries

    def __str__(self):
        return self.user.user_name + "'s Itinerary"

class CityItinerary(models.Model): # Represents a specific city itinerary in a User Itinerary.
    userItinerary=models.ForeignKey(UserItinerary, on_delete=models.CASCADE) # A CityItinerary can belong to only one User Itinerary.
    places=models.ManyToManyField(Place) # A cityItinerary can have many Places. And a Place can be a part of many CityItineraries
    start_date = models.DateTimeField()
    num_days = models.IntegerField(default=0)

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




