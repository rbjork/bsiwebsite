# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Counties(models.Model):
    fip = models.CharField(db_column='FIP', primary_key=True, max_length=7)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
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
