# Generated by Django 2.0.3 on 2018-04-17 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('please_website_app', '0039_city_cm_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(blank=True, max_length=5000, null=True)),
                ('author', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]