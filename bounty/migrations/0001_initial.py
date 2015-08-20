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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, default=5.0, max_digits=6)),
                ('creation_date', models.DateTimeField(verbose_name='date created', default=datetime.datetime.now)),
                ('expiration_date', models.DateTimeField(verbose_name='expiration date', null=True)),
                ('item_count', models.IntegerField(default=0)),
                ('is_saved', models.BooleanField(default=False)),
                ('is_claimed', models.BooleanField(default=False)),
                ('is_requested', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BountyItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
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
        migrations.CreateModel(
            name='ChowBountyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('special_instructions', models.CharField(max_length=100)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='bounty',
            name='cb_user',
            field=models.ForeignKey(to='bounty.ChowBountyUser'),
            preserve_default=True,
        ),
    ]
