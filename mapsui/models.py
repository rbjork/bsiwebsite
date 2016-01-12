#from django.db import models
from django.contrib.gis.db import models # as adminmodels
from django.contrib.gis import admin

class StateMap(models.Model):
    geometry = models.MultiPolygonField(srid=4326)
    name = models.CharField(db_column='STATE', max_length=2, blank=True, null=True) #models.CharField(max_length=2)
    def __str__(self):
        return self.name

# Create your models here.
class CountyMap(models.Model):
    geometry = models.MultiPolygonField(srid=4326)
    fip = models.CharField(db_column='FIP', primary_key=True, max_length=7)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=2, blank=True, null=True) #models.ForeignKey(State)
    county = models.CharField(db_column='COUNTY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='VERSION', max_length=16, blank=True, null=True)  # Field name made lowercase.
    comp = models.CharField(db_column='COMP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    apnpercent = models.CharField(db_column='APNPercent', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sitpercent = models.CharField(db_column='SITPercent', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ownpercent = models.CharField(db_column='OWNPercent', max_length=4, blank=True, null=True)  # Field name made lowercase.
    usepercent = models.CharField(db_column='USEPercent', max_length=4, blank=True, null=True)  # Field name made lowercase.
    valpercent = models.CharField(db_column='VALPercent', max_length=4, blank=True, null=True)  # Field name made lowercase.
    flrpercent = models.CharField(db_column='FLRPercent', max_length=4, blank=True, null=True)  # Field name made lowercase.
    untpercent = models.CharField(db_column='UNTPercent', max_length=4, blank=True, null=True)  # Field name made lowercase.
    yrbpercent = models.CharField(db_column='YRBPercent', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Counties'

    def __str__(self):
        return {'county':self.county,'state':self.state}




class GeoLocationAdmin(admin.OSMGeoAdmin):
    list_display = ('name','interestingness')
    list_filter = ('name','interestingness',)
    fieldsets = (
        ('Location Attributes', {'fields': (('name','interestingness'))}),
       ('Editable Map View', {'fields': ('geometry',)}),
    )

    # Default GeoDjango OpenLayers map options
    scrollable = False
    map_width = 700
    map_height = 325

class GeoLocation(models.Model):
    name = models.CharField(max_length=50, )
    description = models.TextField()
    interestingness = models.IntegerField()
    geometry = models.PointField(srid=4326) #EPSG:4236 is the spatial reference for our data
    objects = models.GeoManager() # so we can use spatial queryset methods

    def __unicode__(self): return self.name