# Generated by Django 3.1.7 on 2021-04-12 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20210412_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='makerequest',
            name='order_id',
            field=models.CharField(default=0, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='makerequestcash',
            name='order_id',
            field=models.CharField(default=0, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='shopping',
            name='order_id',
            field=models.CharField(default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Canceled', 'Canceled'), ('Pending', 'Pending'), ('At the Mall', 'At the Mall')], default='Pending', max_length=20, null=True),
        ),
    ]
