# Generated by Django 3.1.7 on 2021-05-27 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0052_auto_20210527_1225'),
    ]

    operations = [
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
            model_name='makerequestcash',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Canceled', 'Canceled'), ('Pending', 'Pending'), ('Delivered', 'Delivered')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='status',
            field=models.CharField(choices=[('At the Mall', 'At the Mall'), ('Canceled', 'Canceled'), ('Pending', 'Pending'), ('Delivered', 'Delivered')], default='Pending', max_length=20, null=True),
        ),
    ]
