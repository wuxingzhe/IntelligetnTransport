# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-14 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StreetCrowd', '0002_auto_20180205_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='PointsPrediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('virsual_val', models.IntegerField()),
                ('frame_id', models.IntegerField()),
                ('coord_id', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='carstatus',
            name='direction',
        ),
        migrations.RemoveField(
            model_name='carstatus',
            name='time',
        ),
        migrations.AlterField(
            model_name='carstatus',
            name='speed',
            field=models.FloatField(default=0.0),
        ),
    ]
