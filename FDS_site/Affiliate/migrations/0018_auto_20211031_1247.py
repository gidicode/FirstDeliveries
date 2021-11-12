# Generated by Django 3.1.7 on 2021-10-31 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Affiliate', '0017_auto_20211029_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referrals',
            name='Delivery_status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Canceled', 'Canceled')], editable=False, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='request_payout',
            name='Payment_status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Pending', 'Pending'), ('Canceled', 'Canceled')], default='Pending', max_length=10, null=True),
        ),
    ]
