# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-07 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('please_website_app', '0006_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='position_type',
            field=models.CharField(choices=[('Intern', 'Intern'), ('Full-Time', 'Full-Time')], default='Full-Time', max_length=20),
        ),
    ]
