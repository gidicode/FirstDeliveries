# Generated by Django 3.1.7 on 2021-06-03 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0066_auto_20210603_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anonymous',
            name='Amount_Paid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='anonymous',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled'), ('Pending', 'Pending')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='makerequest',
            name='Amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='makerequest',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled'), ('Pending', 'Pending')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='Amount_Paid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled'), ('Pending', 'Pending')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='Amount',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Enter an estimated amount, our charges Inclusive', max_digits=10),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='Amount_Refunded',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='Charge',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='Item_Cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='Total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='amount_paid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Canceled', 'Canceled'), ('At the Mall', 'At the Mall'), ('Pending', 'Pending')], default='Pending', max_length=20, null=True),
        ),
    ]
