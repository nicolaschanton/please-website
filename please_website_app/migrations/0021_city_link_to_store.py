# Generated by Django 2.0.3 on 2018-03-28 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('please_website_app', '0020_teammember_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='link_to_store',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
