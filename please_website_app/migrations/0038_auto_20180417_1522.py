# Generated by Django 2.0.3 on 2018-04-17 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('please_website_app', '0037_auto_20180417_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='gps_coordinates',
            field=models.CharField(blank=True, max_length=500000, null=True),
        ),
    ]