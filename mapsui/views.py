from django.shortcuts import render

# Create your views here.
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.utils import mapping, LayerMapping
from django.shortcuts import get_object_or_404
from .models import StateMap,CountyMap

from django.shortcuts import render_to_response
from django.contrib.gis.shortcuts import render_to_kml
from .models import *

def import_state_shape(file):
    states = DataSource(file)
    lm = LayerMapping(StateMap, states, mapping(states, geom_name='geometry'))
    lm.save(verbose=True)

def import_county_shape(file):
    counties = DataSource(file)
    lm = LayerMapping(CountyMap, counties, mapping(counties, geom_name='geometry'))
    lm.save(verbose=True) # Saves to database - need to first migrate County and State model to database

def display_county(request,id):
    county = get_object_or_404(CountyMap,pk=id)

def all_kml(request):
     locations  = GeoLocation.objects.kml()
     return render_to_kml("placemarks.kml", {'places' : locations})

def map_page(request):
     lcount = GeoLocation.objects.all().count()
     return render_to_response('map.html', {'location_count' : lcount})