# Generated by Django 3.1.7 on 2021-11-13 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortHarcourt', '0034_auto_20211101_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errand_service_ph',
            name='Shawarma_desc',
            field=models.CharField(choices=[('Special', 'Special'), ('Beef', 'Beef'), ('Chicken', 'Chicken')], max_length=100, null=True, verbose_name='Preference'),
        ),
        migrations.AlterField(
            model_name='errand_service_ph',
            name='category',
            field=models.CharField(choices=[('Drugs', 'Drugs'), ('Bread', 'Bread'), ('Pizza', 'Pizza'), ('Food', 'Food'), ('Fruits', 'Fruits'), ('Others', 'Others'), ('Ice Cream', 'Ice Cream'), ('Fuel', 'Fuel'), ('Shawarma', 'Shawarma'), ('Gas', 'Gas')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='errand_service_ph',
            name='status',
            field=models.CharField(choices=[('On Route for Delivery', 'On route for Delivery'), ('Pending', 'Pending'), ('Delivered', 'Delivered'), ('Purchase in Process', 'Purchase in Process')], default='Pending', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='front_desk_ph',
            name='customer_payment_method',
            field=models.CharField(choices=[('Card', 'Card'), ('Cash', 'Cash'), ('Transfer', 'Transfer'), ('Transfer & Cash', 'Transfer & Cash')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='front_desk_ph',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Canceled', 'Canceled'), ('Delivered', 'Delivered'), ('Out for delivery', 'Out for delivery')], default='Pending', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='makerequestcash_ph',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Canceled', 'Canceled'), ('Delivered', 'Delivered'), ('Out for delivery', 'Out for delivery')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='shopping_ph',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Canceled', 'Canceled'), ('At the Mall', 'At the Mall'), ('Delivered', 'Delivered')], default='Pending', max_length=20, null=True),
        ),
    ]
