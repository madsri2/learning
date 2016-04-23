from django.conf.urls import url
from . import views

app_name='travel'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^destination/$', views.destination, name='destination'),
    url(r'^destination/city/$',views.cities, name='cities'),
    url(r'^plan/$', views.plan, name='plan'),
    url(r'^destination/(?P<tripId>[a-zA-Z]+)/places/$',views.places, name='places'),
    url(r'^destination/(?P<tripId>[a-zA-Z]+)/itinerary/$',views.itinerary, name='itinerary')
]
