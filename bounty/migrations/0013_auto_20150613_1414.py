# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.contrib.gis.db.models.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bounty', '0012_auto_20150611_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('line1', models.CharField(max_length=100)),
                ('line2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('zipcode_str', models.CharField(max_length=5)),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BountyHunter',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('photo_link', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ChowBountyUser',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('special_instructions', models.CharField(max_length=100)),
                ('address', models.ForeignKey(to='bounty.Address')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('address', models.ForeignKey(to='bounty.Address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Zipcode',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('code', models.CharField(max_length=5)),
                ('poly', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='bountyhunter',
            name='cb_user',
            field=models.ForeignKey(to='bounty.ChowBountyUser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='zipcode',
            field=models.ForeignKey(to='bounty.Zipcode'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bounty',
            name='creation_date',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime(2015, 6, 13, 14, 14, 27, 292731)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bounty',
            name='expiration_date',
            field=models.DateTimeField(verbose_name='expiration date', default=datetime.datetime(2015, 6, 20, 14, 14, 27, 292731)),
            preserve_default=True,
        ),
    ]
