# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bounty', '0023_auto_20150614_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bounty',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 14, 19, 3, 2, 133385), verbose_name='date created'),
            preserve_default=True,
        ),
    ]
