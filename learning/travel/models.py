import datetime

# Create your models here.
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

class Activities(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type

class User(models.Model):
    name = models.CharField(max_length=20)
    # A user can have many activities and an activity can be part of many users. See https://docs.djangoproject.com/ja/1.9/topics/db/models/#many-to-many-relationships
    activities=models.ManyToManyField(Activities)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country,
                                on_delete=models.CASCADE)  # A city can belong to only one country. A country can have many cities.

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City,
                             on_delete=models.CASCADE)  # A place can belong to only one city. A city can have many places
    type = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class UserItinerary(models.Model): # Represents a list of cities that a user wants to travel to.
    user = models.ForeignKey(User, on_delete=models.CASCADE) # An itinerary can only have one user. A user can have many itineraries

    def __str__(self):
        return self.user.name + "'s Itinerary"

class CityItinerary(models.Model): # Represents a specific city itinerary in a User Itinerary.
    userItinerary=models.ForeignKey(UserItinerary, on_delete=models.CASCADE) # A CityItinerary can belong to only one User Itinerary.
    city=models.ForeignKey(City, on_delete=models.CASCADE) #A cityItinerary can belongs to only one city.
    places=models.ManyToManyField(Place) # A cityItinerary can have many Places.  A Place can be a part of many CityItineraries
    start_date = models.DateField()
    end_date = models.DateField()
    # num_days = models.IntegerField(default=0)

    def __str__(self):
        return self.userItinerary.user.name + "'s " + self.city.name + " itinerary from " + \
               self.start_date.strftime('%m/%d/%y') + " to " + self.end_date.strftime('%m/%d/%y')

class Itinerary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source_city = models.CharField(max_length=50)
    dest_city = models.CharField(max_length=50)
    start_date = models.DateField()
    num_days = models.IntegerField(default=0)

    def __str__(self):
        return self.user.user_name + ":" + self.source_city + " to " + self.dest_city

    def travelling_soon(self):
        return self.start_date >= timezone.now() + datetime.timedelta(days=20)




