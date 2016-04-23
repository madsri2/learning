from django.shortcuts import render
from django.http import HttpResponse
from django import forms

import datetime

from .models import User
from .models import Itinerary

# Create your views here.
def index(request):
	return HttpResponse("First step for me!")

class CountryForm(forms.Form):
    country=forms.CharField(label='Where do you want to go', max_length=100)

class CityForm(forms.Form):
    city=forms.CharField(label="City")
    startDate=forms.DateField()
    numDays = forms.IntegerField()

class EmptyForm(forms.Form):
    e=forms.CharField(label='E')

def destination(request):
    form = CountryForm()
    return render(request, 'travel/index.html', {'form': form})

def cities(request):
    form=EmptyForm(request.POST)
    #if form.is_valid():
    cityForm = CityForm()
    #    return render(request, 'travel/cities.html', {'form': cityForm})
    #    return HttpResponse("Yup")
    #else:
    e = EmptyForm()
    return render(request, 'travel/cities.html', {'form': e, 'user': "Hello"})

        # "You are going to %s !" % form.cleaned_data['country'])

def plan(request):
    user_id=User.objects.get(user_name="aparnara").id
    itin=Itinerary.objects.get(user=user_id)
    end_date = itin.start_date + datetime.timedelta(days=itin.num_days)
    return render(request, 'travel/plan.html', {'itin': itin, 'end_date': end_date})

def places(request,tripId):
    return HttpResponse("You will enter places for trip %s here" % tripId)

def itinerary(request,tripId):
    return HttpResponse("This is where your itinerary for trip %s will be listed" % tripId)
