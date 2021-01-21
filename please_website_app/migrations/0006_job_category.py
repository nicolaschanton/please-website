# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-07 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('please_website_app', '0005_job_teammember'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='category',
            field=models.CharField(choices=[('Marketing & Sales', 'Marketing & Sales'), ('Tech', 'Tech'), ('Product', 'Product'), ('Operations', 'Operations'), ('Admin', 'Admin')], default='Marketing & Sales', max_length=20),
        ),
    ]