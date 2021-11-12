# Generated by Django 3.1.7 on 2021-04-19 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0031_auto_20210419_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivered',
            name='order_id',
            field=models.CharField(default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='makerequest',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Canceled', 'Canceled')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Canceled', 'Canceled')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Canceled', 'Canceled'), ('At the Mall', 'At the Mall')], default='Pending', max_length=20, null=True),
        ),
    ]
