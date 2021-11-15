# Generated by Django 3.1.7 on 2021-11-15 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortHarcourt', '0035_auto_20211113_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errand_service_ph',
            name='Shawarma_desc',
            field=models.CharField(choices=[('Beef', 'Beef'), ('Special', 'Special'), ('Chicken', 'Chicken')], max_length=100, null=True, verbose_name='Preference'),
        ),
        migrations.AlterField(
            model_name='errand_service_ph',
            name='category',
            field=models.CharField(choices=[('Shawarma', 'Shawarma'), ('Pizza', 'Pizza'), ('Gas', 'Gas'), ('Fuel', 'Fuel'), ('Food', 'Food'), ('Fruits', 'Fruits'), ('Bread', 'Bread'), ('Drugs', 'Drugs'), ('Others', 'Others'), ('Ice Cream', 'Ice Cream')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='errand_service_ph',
            name='status',
            field=models.CharField(choices=[('Purchase in Process', 'Purchase in Process'), ('Delivered', 'Delivered'), ('On Route for Delivery', 'On route for Delivery'), ('Pending', 'Pending')], default='Pending', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='front_desk_ph',
            name='customer_payment_method',
            field=models.CharField(choices=[('Transfer & Cash', 'Transfer & Cash'), ('Cash', 'Cash'), ('Transfer', 'Transfer'), ('Card', 'Card')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='front_desk_ph',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Canceled', 'Canceled')], default='Pending', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='makerequestcash_ph',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Canceled', 'Canceled')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='shopping_ph',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('At the Mall', 'At the Mall'), ('Pending', 'Pending'), ('Canceled', 'Canceled')], default='Pending', max_length=20, null=True),
        ),
    ]
