from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("First step for me!")

def destination(request):
	return HttpResponse("You will enter countries, cities and places you want to visit here")

def itinerary(request):
	return HttpResponse("This is where your itinerary will be listed")
