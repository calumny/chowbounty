# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bounty', '0020_auto_20150614_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bounty',
            name='creation_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 6, 14, 15, 57, 55, 579421)),
            preserve_default=True,
        ),
    ]
