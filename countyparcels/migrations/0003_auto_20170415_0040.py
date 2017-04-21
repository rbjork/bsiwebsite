# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countyparcels', '0002_auto_20151102_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='counties',
            name='flrpercent',
        ),
        migrations.RemoveField(
            model_name='counties',
            name='untpercent',
        ),
        migrations.RemoveField(
            model_name='counties',
            name='yrbpercent',
        ),
        migrations.AddField(
            model_name='counties',
            name='status',
            field=models.CharField(max_length=20, null=True, db_column=b'STATUS', blank=True),
        ),
        migrations.AlterField(
            model_name='counties',
            name='apnpercent',
            field=models.CharField(max_length=15, null=True, db_column=b'APNPercent', blank=True),
        ),
        migrations.AlterField(
            model_name='counties',
            name='ownpercent',
            field=models.CharField(max_length=15, null=True, db_column=b'OWNPercent', blank=True),
        ),
        migrations.AlterField(
            model_name='counties',
            name='sitpercent',
            field=models.CharField(max_length=15, null=True, db_column=b'SITPercent', blank=True),
        ),
        migrations.AlterField(
            model_name='counties',
            name='usepercent',
            field=models.CharField(max_length=15, null=True, db_column=b'USEPercent', blank=True),
        ),
        migrations.AlterField(
            model_name='counties',
            name='valpercent',
            field=models.CharField(max_length=15, null=True, db_column=b'VALPercent', blank=True),
        ),
    ]
