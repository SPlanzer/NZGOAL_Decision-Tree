# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('answer', models.CharField(max_length=3, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dataSetName', models.CharField(max_length=200)),
                ('dmName', models.CharField(max_length=200)),
                ('treeComplete', models.BooleanField(default=False)),
                ('ldsId', models.CharField(max_length=10, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qid', models.CharField(max_length=2)),
                ('question', models.CharField(max_length=1500)),
                ('y', models.CharField(max_length=2)),
                ('n', models.CharField(max_length=2)),
                ('isquestion', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='dataSet',
            field=models.ForeignKey(to='dtree.DataSet'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='dtree.Question'),
        ),
    ]
