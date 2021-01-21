# Generated by Django 2.0.3 on 2018-04-11 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('please_website_app', '0032_city_conciergerie_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merchant',
            name='percentage',
        ),
        migrations.RemoveField(
            model_name='merchant',
            name='siret',
        ),
        migrations.AddField(
            model_name='merchant',
            name='competition',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='merchant',
            name='interested',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]