# Generated by Django 3.1.7 on 2021-12-10 14:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('PortHarcourt', '0037_auto_20211210_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='PH_Fleets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fleet_plate_number', models.CharField(max_length=100, null=True)),
                ('Tracker_id', models.CharField(max_length=100, null=True)),
                ('Tracker_phone_num', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(choices=[('Bike', 'Bike'), ('Tricycle', 'Tricycle')], max_length=100, null=True)),
                ('vechile_name', models.CharField(max_length=100, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='errand_service_ph',
            name='category',
            field=models.CharField(choices=[('Food', 'Food'), ('Pizza', 'Pizza'), ('Drugs', 'Drugs'), ('Others', 'Others'), ('Bread', 'Bread'), ('Fruits', 'Fruits'), ('Ice Cream', 'Ice Cream'), ('Gas', 'Gas'), ('Shawarma', 'Shawarma'), ('Fuel', 'Fuel')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='errand_service_ph',
            name='status',
            field=models.CharField(choices=[('On Route for Delivery', 'On route for Delivery'), ('Pending', 'Pending'), ('Delivered', 'Delivered'), ('Purchase in Process', 'Purchase in Process')], default='Pending', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='front_desk_ph',
            name='customer_payment_method',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Transfer', 'Transfer'), ('Transfer & Cash', 'Transfer & Cash'), ('Card', 'Card')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='front_desk_ph',
            name='status',
            field=models.CharField(choices=[('Canceled', 'Canceled'), ('Pending', 'Pending'), ('Delivered', 'Delivered'), ('Out for delivery', 'Out for delivery')], default='Pending', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='makerequestcash_ph',
            name='status',
            field=models.CharField(choices=[('Canceled', 'Canceled'), ('Pending', 'Pending'), ('Delivered', 'Delivered'), ('Out for delivery', 'Out for delivery')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='shopping_ph',
            name='status',
            field=models.CharField(choices=[('Canceled', 'Canceled'), ('Pending', 'Pending'), ('At the Mall', 'At the Mall'), ('Delivered', 'Delivered')], default='Pending', max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='PH_RidersProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=17, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,12}$')])),
                ('Address', models.CharField(max_length=100, null=True)),
                ('verified_gurantor', models.BooleanField(default=False)),
                ('gurantor_name', models.CharField(max_length=100, null=True)),
                ('gurantor_address', models.CharField(max_length=100, null=True)),
                ('Riders_profile', models.CharField(max_length=100, null=True)),
                ('busy', models.BooleanField(default=False)),
                ('attached_bike', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PortHarcourt.ph_fleets')),
            ],
        ),
    ]
