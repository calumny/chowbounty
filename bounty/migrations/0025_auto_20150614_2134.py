# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bounty', '0024_auto_20150614_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='bounty',
            name='address',
            field=models.ForeignKey(to='bounty.Address', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bounty',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 14, 21, 34, 28, 716314), verbose_name='date created'),
            preserve_default=True,
        ),
    ]
