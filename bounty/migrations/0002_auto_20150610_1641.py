# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bounty', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bounty',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='bounty',
            name='expiration_date',
        ),
        migrations.RemoveField(
            model_name='bounty',
            name='is_claimed',
        ),
        migrations.RemoveField(
            model_name='bounty',
            name='is_requested',
        ),
        migrations.RemoveField(
            model_name='bounty',
            name='is_saved',
        ),
    ]
