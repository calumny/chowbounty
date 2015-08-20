# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bounty', '0026_auto_20150614_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='street',
            field=models.CharField(null=True, max_length=100),
            preserve_default=True,
        ),
    ]
