# Generated by Django 3.1.7 on 2021-04-12 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20210412_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makerequest',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Out for delivery', 'Out for delivery'), ('Pending', 'Pending'), ('Canceled', 'Canceled')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Out for delivery', 'Out for delivery'), ('Pending', 'Pending'), ('Canceled', 'Canceled')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Pending', 'Pending'), ('At the Mall', 'At the Mall'), ('Canceled', 'Canceled')], default='Pending', max_length=20, null=True),
        ),
    ]
