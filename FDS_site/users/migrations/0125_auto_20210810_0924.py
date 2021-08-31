# Generated by Django 3.1.7 on 2021-08-10 08:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BikeControl', '0007_auto_20210726_1203'),
        ('users', '0124_auto_20210806_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anonymous',
            name='customer_payment_method',
            field=models.CharField(choices=[('Transfer & Cash', 'Transfer & Cash'), ('Card', 'Card'), ('Cash', 'Cash'), ('Transfer', 'Transfer')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='anonymous',
            name='riders',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='BikeControl.ridersprofile'),
        ),
        migrations.AlterField(
            model_name='anonymous',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Canceled', 'Canceled'), ('Delivered', 'Delivered')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='errand_service',
            name='Shawarma_desc',
            field=models.CharField(choices=[('Special', 'Special'), ('Beef', 'Beef'), ('Chicken', 'Chicken')], max_length=100, null=True, verbose_name='Preference'),
        ),
        migrations.AlterField(
            model_name='errand_service',
            name='category',
            field=models.CharField(choices=[('Pizza', 'Pizza'), ('Gas', 'Gas'), ('Drugs', 'Drugs'), ('Ice Cream', 'Ice Cream'), ('Bread', 'Bread'), ('Food', 'Food'), ('Others', 'Others'), ('Fuel', 'Fuel'), ('Shawarma', 'Shawarma'), ('Fruits', 'Fruits')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='errand_service',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered'), ('Purchase in Process', 'Purchase in Process'), ('On Route for Delivery', 'On route for Delivery')], default='Pending', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='front_desk',
            name='Customer_phone_number',
            field=models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')], verbose_name='Customer Phone Number'),
        ),
        migrations.AlterField(
            model_name='front_desk',
            name='Enter_amount',
            field=models.IntegerField(blank=True, help_text='Cost to purchase items', null=True, verbose_name='Item Amount'),
        ),
        migrations.AlterField(
            model_name='front_desk',
            name='customer_payment_method',
            field=models.CharField(choices=[('Transfer & Cash', 'Transfer & Cash'), ('Card', 'Card'), ('Cash', 'Cash'), ('Transfer', 'Transfer')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='front_desk',
            name='riders',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='BikeControl.ridersprofile'),
        ),
        migrations.AlterField(
            model_name='front_desk',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Canceled', 'Canceled'), ('Delivered', 'Delivered')], default='Pending', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='makerequest',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Canceled', 'Canceled'), ('Delivered', 'Delivered')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Canceled', 'Canceled'), ('Delivered', 'Delivered')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('At the Mall', 'At the Mall'), ('Canceled', 'Canceled'), ('Delivered', 'Delivered')], default='Pending', max_length=20, null=True),
        ),
    ]
