# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bounty', '0015_auto_20150613_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chowbountyuser',
            name='name',
        ),
        migrations.AlterField(
            model_name='bounty',
            name='creation_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 6, 13, 15, 29, 24, 790783)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bounty',
            name='expiration_date',
            field=models.DateTimeField(verbose_name='expiration date', default=datetime.datetime(2015, 6, 20, 15, 29, 24, 790783)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chowbountyuser',
            name='address',
            field=models.ForeignKey(to='bounty.Address', null=True),
            preserve_default=True,
        ),
    ]
