# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countyparcels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counties',
            name='apnpercent',
            field=models.IntegerField(null=True, db_column=b'APNPercent', blank=True),
        ),
        migrations.AlterField(
            model_name='counties',
            name='comp',
            field=models.IntegerField(null=True, db_column=b'COMP', blank=True),
        ),
        migrations.AlterField(
            model_name='counties',
            name='flrpercent',
            field=models.IntegerField(null=True, db_column=b'FLRPercent', blank=True),
        ),
        migrations.AlterField(
            model_name='counties',
            name='ownpercent',
            field=models.IntegerField(null=True, db_column=b'OWNPercent', blank=True),
        ),
        migrations.AlterField(
            model_name='counties',
            name='sitpercent',
            field=models.IntegerField(null=True, db_column=b'SITPercent', blank=True),
        ),
        migrations.AlterField(
            model_name='counties',
            name='untpercent',
            field=models.IntegerField(null=True, db_column=b'UNTPercent', blank=True),
        ),
        migrations.AlterField(
            model_name='counties',
            name='usepercent',
            field=models.IntegerField(null=True, db_column=b'USEPercent', blank=True),
        ),
        migrations.AlterField(
            model_name='counties',
            name='valpercent',
            field=models.IntegerField(null=True, db_column=b'VALPercent', blank=True),
        ),
        migrations.AlterField(
            model_name='counties',
            name='yrbpercent',
            field=models.IntegerField(null=True, db_column=b'YRBPercent', blank=True),
        ),
    ]
