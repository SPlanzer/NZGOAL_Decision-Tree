# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-27 05:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dtree', '0010_auto_20160927_0337'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='progress',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
