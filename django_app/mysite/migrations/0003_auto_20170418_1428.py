# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-18 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20170418_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bilateral',
            name='country_dest_id',
            field=models.CharField(max_length=200),
        ),
    ]
