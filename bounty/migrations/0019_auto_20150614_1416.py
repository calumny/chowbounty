# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bounty', '0018_auto_20150614_1416'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bounty',
            old_name='user',
            new_name='cb_user',
        ),
        migrations.AlterField(
            model_name='bounty',
            name='creation_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 6, 14, 14, 16, 52, 300336)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bounty',
            name='expiration_date',
            field=models.DateTimeField(verbose_name='expiration date', default=datetime.datetime(2015, 6, 21, 14, 16, 52, 300336)),
            preserve_default=True,
        ),
    ]
