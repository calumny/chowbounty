# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bounty', '0003_auto_20150610_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='bounty',
            name='price',
            field=models.DecimalField(default=5.0, decimal_places=2, max_digits=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bounty',
            name='creation_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 6, 10, 19, 58, 9, 515667)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bounty',
            name='expiration_date',
            field=models.DateTimeField(verbose_name='expiration date', default=datetime.datetime(2015, 6, 17, 19, 58, 9, 515667)),
            preserve_default=True,
        ),
    ]
