# Generated by Django 3.1.7 on 2021-10-11 16:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Affiliate', '0002_auto_20211009_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiliate_group',
            name='Amount_Credited',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='affiliate_group',
            name='Amount_Genreated',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='affiliate_group',
            name='Date_Joined',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='affiliate_group',
            name='Profit_Generated',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='affiliate_group',
            name='Total_Referal',
            field=models.IntegerField(default=0, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='affiliate_group',
            name='Wallet_Balance',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=6, null=True),
        ),
    ]
