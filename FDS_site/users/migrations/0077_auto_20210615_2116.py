# Generated by Django 3.1.7 on 2021-06-15 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0076_auto_20210613_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='makerequest',
            name='Area',
        ),
        migrations.RemoveField(
            model_name='makerequest',
            name='Area_2',
        ),
        migrations.RemoveField(
            model_name='makerequest',
            name='Area_3',
        ),
        migrations.RemoveField(
            model_name='makerequest',
            name='Area_4',
        ),
        migrations.RemoveField(
            model_name='makerequest',
            name='Area_5',
        ),
        migrations.RemoveField(
            model_name='makerequest',
            name='Your_area',
        ),
        migrations.RemoveField(
            model_name='makerequestcash',
            name='Area',
        ),
        migrations.RemoveField(
            model_name='makerequestcash',
            name='Area_2',
        ),
        migrations.RemoveField(
            model_name='makerequestcash',
            name='Area_3',
        ),
        migrations.RemoveField(
            model_name='makerequestcash',
            name='Area_4',
        ),
        migrations.RemoveField(
            model_name='makerequestcash',
            name='Area_5',
        ),
        migrations.RemoveField(
            model_name='makerequestcash',
            name='Your_area',
        ),
        migrations.AlterField(
            model_name='anonymous',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Canceled', 'Canceled'), ('Pending', 'Pending'), ('Delivered', 'Delivered')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='makerequest',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Canceled', 'Canceled'), ('Pending', 'Pending'), ('Delivered', 'Delivered')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='makerequest',
            name='type',
            field=models.CharField(choices=[('Multiple', 'Multiple'), ('Single', 'Single')], default='Single', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Canceled', 'Canceled'), ('Pending', 'Pending'), ('Delivered', 'Delivered')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='type',
            field=models.CharField(choices=[('Multiple', 'Multiple'), ('Single', 'Single')], default='Single', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='status',
            field=models.CharField(choices=[('Canceled', 'Canceled'), ('Pending', 'Pending'), ('Delivered', 'Delivered'), ('At the Mall', 'At the Mall')], default='Pending', max_length=20, null=True),
        ),
    ]
