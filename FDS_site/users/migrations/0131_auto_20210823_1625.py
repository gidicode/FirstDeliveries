# Generated by Django 3.1.7 on 2021-08-23 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0130_auto_20210823_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anonymous',
            name='customer_payment_method',
            field=models.CharField(choices=[('Card', 'Card'), ('Transfer', 'Transfer'), ('Cash', 'Cash'), ('Transfer & Cash', 'Transfer & Cash')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='anonymous',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Canceled', 'Canceled'), ('Out for delivery', 'Out for delivery'), ('Pending', 'Pending')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Department',
            field=models.CharField(choices=[(None, None), ('FIRST LOGISTICS', 'FIRST LOGISTICS'), ('FIRST MARINE', 'FIRST MARINE')], default=None, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Designation',
            field=models.CharField(choices=[(None, None), ('MARKETING', 'MARKETING'), ('ICT', 'ICT'), ('FLEET MANAGER', 'FLEET MANAGER'), ('FRONT DESK', 'FRONT DESK'), ('ADMIN', 'ADMIN'), ('MANAGER', 'MANAGER'), ('ACCOUNT', 'ACCOUNT')], default='ACCOUNT', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='errand_service',
            name='Shawarma_desc',
            field=models.CharField(choices=[('Special', 'Special'), ('Chicken', 'Chicken'), ('Beef', 'Beef')], max_length=100, null=True, verbose_name='Preference'),
        ),
        migrations.AlterField(
            model_name='errand_service',
            name='category',
            field=models.CharField(choices=[('Drugs', 'Drugs'), ('Food', 'Food'), ('Others', 'Others'), ('Fruits', 'Fruits'), ('Fuel', 'Fuel'), ('Shawarma', 'Shawarma'), ('Ice Cream', 'Ice Cream'), ('Gas', 'Gas'), ('Bread', 'Bread'), ('Pizza', 'Pizza')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='errand_service',
            name='status',
            field=models.CharField(choices=[('On Route for Delivery', 'On route for Delivery'), ('Delivered', 'Delivered'), ('Purchase in Process', 'Purchase in Process'), ('Pending', 'Pending')], default='Pending', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='front_desk',
            name='customer_payment_method',
            field=models.CharField(choices=[('Card', 'Card'), ('Transfer', 'Transfer'), ('Cash', 'Cash'), ('Transfer & Cash', 'Transfer & Cash')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='front_desk',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Canceled', 'Canceled'), ('Out for delivery', 'Out for delivery'), ('Pending', 'Pending')], default='Pending', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='makerequest',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Canceled', 'Canceled'), ('Out for delivery', 'Out for delivery'), ('Pending', 'Pending')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='makerequest',
            name='type',
            field=models.CharField(choices=[('Multiple', 'Multiple'), ('Single', 'Single')], default='Single', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Canceled', 'Canceled'), ('Out for delivery', 'Out for delivery'), ('Pending', 'Pending')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='type',
            field=models.CharField(choices=[('Multiple', 'Multiple'), ('Single', 'Single')], default='Single', max_length=50, null=True),
        ),
    ]
