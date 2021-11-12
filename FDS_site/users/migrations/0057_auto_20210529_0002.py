# Generated by Django 3.1.7 on 2021-05-28 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0056_auto_20210529_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anonymous',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Canceled', 'Canceled')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='makerequest',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Canceled', 'Canceled')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Canceled', 'Canceled')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='status',
            field=models.CharField(choices=[('At the Mall', 'At the Mall'), ('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Canceled', 'Canceled')], default='Pending', max_length=20, null=True),
        ),
    ]
