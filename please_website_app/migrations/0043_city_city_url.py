# Generated by Django 2.0.3 on 2018-06-04 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('please_website_app', '0042_auto_20180418_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='city_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
