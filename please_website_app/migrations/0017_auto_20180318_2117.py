# Generated by Django 2.0.3 on 2018-03-18 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('please_website_app', '0016_auto_20180317_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='display_rank',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
