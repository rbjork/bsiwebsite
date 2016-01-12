from django.db import models

# Create your models here.
from django.db import models
'''
class State(models.Model):
    name = models.CharField(db_column='STATE', max_length=2, blank=True, null=True) #models.CharField(max_length=2)
    def __str__(self):
        return self.name
'''
class Counties(models.Model):
    fip = models.CharField(db_column='FIP', primary_key=True, max_length=7)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=2, blank=True, null=True) #models.ForeignKey(State)
    county = models.CharField(db_column='COUNTY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='VERSION', max_length=16, blank=True, null=True)  # Field name made lowercase.
    comp = models.IntegerField(db_column='COMP', blank=True, null=True)  # Field name made lowercase.
    apnpercent = models.IntegerField(db_column='APNPercent', blank=True, null=True)  # Field name made lowercase.
    sitpercent = models.IntegerField(db_column='SITPercent', blank=True, null=True)  # Field name made lowercase.
    ownpercent = models.IntegerField(db_column='OWNPercent', blank=True, null=True)  # Field name made lowercase.
    usepercent = models.IntegerField(db_column='USEPercent', blank=True, null=True)  # Field name made lowercase.
    valpercent = models.IntegerField(db_column='VALPercent', blank=True, null=True)  # Field name made lowercase.
    flrpercent = models.IntegerField(db_column='FLRPercent', blank=True, null=True)  # Field name made lowercase.
    untpercent = models.IntegerField(db_column='UNTPercent', blank=True, null=True)  # Field name made lowercase.
    yrbpercent = models.IntegerField(db_column='YRBPercent', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return {'county':self.county,'state':self.state}

    def loadcsv(self):
        f = open('orderpage.csv', 'r')
        for line in f:
           line =  line.split(';')
           county = Counties()
           county.county = line[2]
           county.state = ""
           county.version = line[3]
           county.comp = line[4]
           county.percentapn = line[5]
           county.percentown = line[6]
           county.uuse = line[7]
           county.flr = line[8]
           county.yrbuilt = line[9]
           county.save()
        f.close()
