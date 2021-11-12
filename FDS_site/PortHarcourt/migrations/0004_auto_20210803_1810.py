# Generated by Django 3.1.7 on 2021-08-03 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortHarcourt', '0003_auto_20210728_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errand_service_ph',
            name='Shawarma_desc',
            field=models.CharField(choices=[('Chicken', 'Chicken'), ('Beef', 'Beef'), ('Special', 'Special')], max_length=100, null=True, verbose_name='Preference'),
        ),
        migrations.AlterField(
            model_name='errand_service_ph',
            name='category',
            field=models.CharField(choices=[('Drugs', 'Drugs'), ('Food', 'Food'), ('Fuel', 'Fuel'), ('Gas', 'Gas'), ('Others', 'Others'), ('Bread', 'Bread'), ('Ice Cream', 'Ice Cream'), ('Fruits', 'Fruits'), ('Pizza', 'Pizza'), ('Shawarma', 'Shawarma')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='errand_service_ph',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('On Route for Delivery', 'On route for Delivery'), ('Pending', 'Pending'), ('Purchase in Process', 'Purchase in Process')], default='Pending', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='makerequestcash_ph',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled'), ('Pending', 'Pending')], default='Pending', max_length=20, null=True),
        ),
    ]
