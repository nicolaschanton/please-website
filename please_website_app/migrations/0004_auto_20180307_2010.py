# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-07 20:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('please_website_app', '0003_testimonials'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Testimonials',
            new_name='Testimonial',
        ),
    ]
