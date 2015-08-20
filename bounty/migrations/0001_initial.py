# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bounty',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('creation_date', models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 6, 10, 15, 1, 51, 492833))),
                ('expiration_date', models.DateTimeField(verbose_name='expiration date', default=datetime.datetime(2015, 6, 17, 15, 1, 51, 492833))),
                ('is_saved', models.BooleanField(default=False)),
                ('is_claimed', models.BooleanField(default=False)),
                ('is_requested', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BountyItem',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('item_name', models.CharField(max_length=100)),
                ('item_quantity', models.IntegerField(default=1)),
                ('image_link', models.CharField(default='', max_length=200)),
                ('save_date', models.DateTimeField(verbose_name='date saved', default=datetime.datetime.now)),
                ('bounty', models.ForeignKey(to='bounty.Bounty')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
