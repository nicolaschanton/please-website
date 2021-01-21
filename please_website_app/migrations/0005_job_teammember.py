# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-07 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('please_website_app', '0004_auto_20180307_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(blank=True, max_length=500, null=True)),
                ('about', models.TextField(blank=True, max_length=5000, null=True)),
                ('job_description', models.ImageField(blank=True, null=True, upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('role', models.TextField(blank=True, max_length=5000, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('linkedin', models.CharField(blank=True, max_length=500, null=True)),
                ('facebook', models.CharField(blank=True, max_length=500, null=True)),
                ('google', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]