# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bounty', '0005_auto_20150610_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorldBorder',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('area', models.IntegerField()),
                ('pop2005', models.IntegerField(verbose_name='Population 2005')),
                ('fips', models.CharField(verbose_name='FIPS Code', max_length=2)),
                ('iso2', models.CharField(verbose_name='2 Digit ISO', max_length=2)),
                ('iso3', models.CharField(verbose_name='3 Digit ISO', max_length=3)),
                ('un', models.IntegerField(verbose_name='United Nations Code')),
                ('region', models.IntegerField(verbose_name='Region Code')),
                ('subregion', models.IntegerField(verbose_name='Sub-Region Code')),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='bounty',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 10, 21, 43, 26, 39130), verbose_name='date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bounty',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 17, 21, 43, 26, 39130), verbose_name='expiration date'),
            preserve_default=True,
        ),
    ]
