# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bounty', '0007_auto_20150610_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bounty',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 11, 18, 16, 27, 124282), verbose_name='date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bounty',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 18, 18, 16, 27, 124282), verbose_name='expiration date'),
            preserve_default=True,
        ),
    ]
