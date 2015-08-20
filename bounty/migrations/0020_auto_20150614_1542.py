# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bounty', '0019_auto_20150614_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='bounty',
            name='coordinates',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bounty',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 14, 15, 42, 44, 309348), verbose_name='date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bounty',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='expiration date'),
            preserve_default=True,
        ),
    ]
