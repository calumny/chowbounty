# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bounty', '0004_auto_20150610_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bounty',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 10, 21, 32, 10, 744064), verbose_name='date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bounty',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 17, 21, 32, 10, 744064), verbose_name='expiration date'),
            preserve_default=True,
        ),
    ]
