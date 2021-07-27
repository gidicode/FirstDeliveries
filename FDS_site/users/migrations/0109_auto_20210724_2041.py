# Generated by Django 3.1.7 on 2021-07-24 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0108_auto_20210723_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='anonymous',
            name='Location',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='anonymous',
            name='status',
            field=models.CharField(choices=[('Canceled', 'Canceled'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Pending', 'Pending')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Location',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='errand_service',
            name='Shawarma_desc',
            field=models.CharField(choices=[('Beef', 'Beef'), ('Special', 'Special'), ('Chicken', 'Chicken')], max_length=100, null=True, verbose_name='Preference'),
        ),
        migrations.AlterField(
            model_name='errand_service',
            name='category',
            field=models.CharField(choices=[('Fruits', 'Fruits'), ('Pizza', 'Pizza'), ('Shawarma', 'Shawarma'), ('Fuel', 'Fuel'), ('Gas', 'Gas'), ('Ice Cream', 'Ice Cream'), ('Food', 'Food'), ('Drugs', 'Drugs'), ('Bread', 'Bread'), ('Others', 'Others')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='errand_service',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('On Route for Delivery', 'On route for Delivery'), ('Pending', 'Pending'), ('Purchase in Process', 'Purchase in Process')], default='Pending', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='front_desk',
            name='status',
            field=models.CharField(choices=[('Canceled', 'Canceled'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Pending', 'Pending')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='makerequest',
            name='status',
            field=models.CharField(choices=[('Canceled', 'Canceled'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Pending', 'Pending')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='status',
            field=models.CharField(choices=[('Canceled', 'Canceled'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Pending', 'Pending')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='status',
            field=models.CharField(choices=[('Canceled', 'Canceled'), ('Pending', 'Pending'), ('Delivered', 'Delivered'), ('At the Mall', 'At the Mall')], default='Pending', max_length=20, null=True),
        ),
    ]
