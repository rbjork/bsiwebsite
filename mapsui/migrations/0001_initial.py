# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountyMap',
            fields=[
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('fip', models.CharField(max_length=7, serialize=False, primary_key=True, db_column=b'FIP')),
                ('state', models.CharField(max_length=2, null=True, db_column=b'STATE', blank=True)),
                ('county', models.CharField(max_length=50, null=True, db_column=b'COUNTY', blank=True)),
                ('version', models.CharField(max_length=16, null=True, db_column=b'VERSION', blank=True)),
                ('comp', models.CharField(max_length=4, null=True, db_column=b'COMP', blank=True)),
                ('apnpercent', models.CharField(max_length=4, null=True, db_column=b'APNPercent', blank=True)),
                ('sitpercent', models.CharField(max_length=4, null=True, db_column=b'SITPercent', blank=True)),
                ('ownpercent', models.CharField(max_length=4, null=True, db_column=b'OWNPercent', blank=True)),
                ('usepercent', models.CharField(max_length=4, null=True, db_column=b'USEPercent', blank=True)),
                ('valpercent', models.CharField(max_length=4, null=True, db_column=b'VALPercent', blank=True)),
                ('flrpercent', models.CharField(max_length=4, null=True, db_column=b'FLRPercent', blank=True)),
                ('untpercent', models.CharField(max_length=4, null=True, db_column=b'UNTPercent', blank=True)),
                ('yrbpercent', models.CharField(max_length=4, null=True, db_column=b'YRBPercent', blank=True)),
            ],
            options={
                'db_table': 'Counties',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GeoLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('interestingness', models.IntegerField()),
                ('geometry', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='StateMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('name', models.CharField(max_length=2, null=True, db_column=b'STATE', blank=True)),
            ],
        ),
    ]
