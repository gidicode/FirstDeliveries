# Generated by Django 3.1.7 on 2021-11-01 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Affiliate', '0018_auto_20211031_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referrals',
            name='Delivery_status',
            field=models.CharField(choices=[('Canceled', 'Canceled'), ('Out for delivery', 'Out for delivery'), ('Pending', 'Pending'), ('Delivered', 'Delivered')], editable=False, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='request_payout',
            name='Payment_status',
            field=models.CharField(choices=[('Canceled', 'Canceled'), ('Paid', 'Paid'), ('Pending', 'Pending')], default='Pending', max_length=10, null=True),
        ),
    ]
