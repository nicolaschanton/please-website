# Generated by Django 2.0.3 on 2018-04-07 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('please_website_app', '0027_merchant_siret'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatecitymanager',
            name='task_completed',
            field=models.NullBooleanField(),
        ),
    ]
