# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-23 00:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dtree', '0004_auto_20160923_0035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='date',
        ),
    ]
