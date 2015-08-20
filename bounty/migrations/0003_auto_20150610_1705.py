# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bounty', '0002_auto_20150610_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='bounty',
            name='creation_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 6, 10, 17, 5, 52, 64668)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bounty',
            name='expiration_date',
            field=models.DateTimeField(verbose_name='expiration date', default=datetime.datetime(2015, 6, 17, 17, 5, 52, 64668)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bounty',
            name='is_claimed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bounty',
            name='is_requested',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bounty',
            name='is_saved',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
