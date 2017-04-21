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
    apnpercent = models.CharField(db_column='APNPercent',max_length=15, blank=True, null=True)  # Field name made lowercase.
    sitpercent = models.CharField(db_column='SITPercent',max_length=15, blank=True, null=True)  # Field name made lowercase.
    ownpercent = models.CharField(db_column='OWNPercent',max_length=15, blank=True, null=True)  # Field name made lowercase.
    usepercent = models.CharField(db_column='USEPercent', max_length=15,blank=True, null=True)  # Field name made lowercase.
    valpercent = models.CharField(db_column='VALPercent',max_length=15, blank=True, null=True)  # Field name made lowercase.
    status     = models.CharField(db_column='STATUS', max_length=20, blank=True, null=True)

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
           county.save()
        f.close()

class Simp(models.Model):
    fip = models.CharField(db_column='FIP', primary_key=True, max_length=7)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=2, blank=True, null=True) #models.ForeignKey(State)
    county = models.CharField(db_column='COUNTY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='VERSION', max_length=16, blank=True, null=True)  # Field name made lowercase.
    comp = models.IntegerField(db_column='COMP', blank=True, null=True)  # Field name made lowercase.
    apnpercent = models.CharField(db_column='APNPercent',max_length=15, blank=True, null=True)  # Field name made lowercase.
    sitpercent = models.CharField(db_column='SITPercent',max_length=15, blank=True, null=True)  # Field name made lowercase.
    ownpercent = models.CharField(db_column='OWNPercent',max_length=15, blank=True, null=True)  # Field name made lowercase.
    usepercent = models.CharField(db_column='USEPercent', max_length=15,blank=True, null=True)  # Field name made lowercase.
    valpercent = models.CharField(db_column='VALPercent',max_length=15, blank=True, null=True)  # Field name made lowercase.
    status     = models.CharField(db_column='STATUS', max_length=20, blank=True, null=True)

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
           county.save()
        f.close()
