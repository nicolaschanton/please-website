# Generated by Django 2.0.3 on 2019-05-14 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('please_website_app', '0044_auto_20190514_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidatecitymanager',
            name='business_number',
        ),
        migrations.RemoveField(
            model_name='candidatecitymanager',
            name='empty_housing_rate',
        ),
        migrations.RemoveField(
            model_name='candidatecitymanager',
            name='housing_price_average',
        ),
        migrations.RemoveField(
            model_name='candidatecitymanager',
            name='service_business_number',
        ),
        migrations.AddField(
            model_name='candidatecitymanager',
            name='activity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='candidatecitymanager',
            name='apport',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='candidatecitymanager',
            name='availability',
            field=models.IntegerField(choices=[(1, 'Immédiate'), (2, 'Dans les 1 à 3 mois'), (3, 'Dans les 3 à 6 mois'), (4, 'Dans plus de 6 mois')], default=1),
        ),
        migrations.AddField(
            model_name='candidatecitymanager',
            name='bakeries',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='candidatecitymanager',
            name='curriculum',
            field=models.TextField(default='', max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidatecitymanager',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='documents/cv/'),
        ),
        migrations.AddField(
            model_name='candidatecitymanager',
            name='project',
            field=models.TextField(default='', max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidatecitymanager',
            name='restaurants',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='candidatecitymanager',
            name='shops_food',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='candidatecitymanager',
            name='shops_service',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
