# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bounty', '0025_auto_20150614_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bounty',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bounty',
            name='expiration_date',
            field=models.DateTimeField(verbose_name='expiration date', null=True),
            preserve_default=True,
        ),
    ]
