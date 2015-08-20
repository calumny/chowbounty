# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bounty', '0021_auto_20150614_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='bounty',
            name='item_count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bounty',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 14, 16, 28, 20, 998258), verbose_name='date created'),
            preserve_default=True,
        ),
    ]
