# Generated by Django 3.1.7 on 2021-10-20 16:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Affiliate', '0012_auto_20211019_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referrals',
            name='Delivery_status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Canceled', 'Canceled'), ('Out for delivery', 'Out for delivery')], editable=False, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='request_payout',
            name='Amount_credited',
            field=models.IntegerField(help_text='Dont input an amount more or less than the debit amount', null=True, verbose_name='Amount to pay'),
        ),
        migrations.AlterField(
            model_name='request_payout',
            name='Payment_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Canceled', 'Canceled')], default='Pending', max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('marketer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Affiliate.affiliate_group')),
            ],
        ),
    ]
