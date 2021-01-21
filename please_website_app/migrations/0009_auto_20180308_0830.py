# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-08 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('please_website_app', '0008_auto_20180307_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='about',
        ),
        migrations.RemoveField(
            model_name='job',
            name='job_description',
        ),
        migrations.AddField(
            model_name='job',
            name='city',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='country',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='link',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]