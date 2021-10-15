# Generated by Django 3.1.7 on 2021-10-14 09:31

import Affiliate.models
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Affiliate', '0008_auto_20211012_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiliate_group',
            name='Amount_Credited',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='affiliate_group',
            name='Profit_Generated',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='affiliate_group',
            name='Wallet_Balance',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='bank_account_details',
            name='Account_Name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bank_account_details',
            name='Account_Number',
            field=models.IntegerField(unique=True, validators=[Affiliate.models.Bank_Account_Details.Check_Len]),
        ),
        migrations.AlterField(
            model_name='referrals',
            name='Delivery_status',
            field=models.CharField(choices=[('Canceled', 'Canceled'), ('Out for delivery', 'Out for delivery'), ('Pending', 'Pending'), ('Delivered', 'Delivered')], editable=False, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='request_payout',
            name='Payment_status',
            field=models.CharField(choices=[('Canceled', 'Canceled'), ('Pending', 'Pending'), ('Paid', 'Paid')], default='Pending', max_length=10, null=True),
        ),
    ]
