# Generated by Django 3.1.7 on 2021-06-15 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0077_auto_20210615_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='anonymous',
            name='Amount_Payable',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='makerequestcash',
            name='Amount_Payable',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='anonymous',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Canceled', 'Canceled')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='makerequest',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Canceled', 'Canceled')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='makerequest',
            name='type',
            field=models.CharField(choices=[('Single', 'Single'), ('Multiple', 'Multiple')], default='Single', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Canceled', 'Canceled')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='type',
            field=models.CharField(choices=[('Single', 'Single'), ('Multiple', 'Multiple')], default='Single', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Pending', 'Pending'), ('At the Mall', 'At the Mall'), ('Canceled', 'Canceled')], default='Pending', max_length=20, null=True),
        ),
    ]
