# Generated by Django 3.1.7 on 2021-05-27 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0049_auto_20210526_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anonymous',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered'), ('Out for delivery', 'Out for delivery'), ('Canceled', 'Canceled')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='makerequest',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered'), ('Out for delivery', 'Out for delivery'), ('Canceled', 'Canceled')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered'), ('Out for delivery', 'Out for delivery'), ('Canceled', 'Canceled')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('At the Mall', 'At the Mall'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled')], default='Pending', max_length=20, null=True),
        ),
    ]
