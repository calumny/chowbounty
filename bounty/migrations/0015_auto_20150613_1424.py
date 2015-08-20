# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bounty', '0014_auto_20150613_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='zipcode',
        ),
        migrations.AlterField(
            model_name='bounty',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 14, 24, 22, 483904), verbose_name='date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bounty',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 14, 24, 22, 483904), verbose_name='expiration date'),
            preserve_default=True,
        ),
    ]
