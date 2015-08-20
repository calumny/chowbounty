# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bounty', '0027_address_street'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(default='', max_length=100),
            preserve_default=True,
        ),
    ]
