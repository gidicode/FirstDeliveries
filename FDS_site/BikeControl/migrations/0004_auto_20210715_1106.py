# Generated by Django 3.1.7 on 2021-07-15 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BikeControl', '0003_auto_20210713_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='ridersprofile',
            name='Riders_profile',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ridersprofile',
            name='busy',
            field=models.BooleanField(default=False),
        ),
    ]
