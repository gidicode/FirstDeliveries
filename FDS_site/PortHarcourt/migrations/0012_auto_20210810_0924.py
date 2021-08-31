# Generated by Django 3.1.7 on 2021-08-10 08:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BikeControl', '0007_auto_20210726_1203'),
        ('users', '0124_auto_20210806_1537'),
        ('PortHarcourt', '0011_auto_20210806_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='errand_service_ph',
            name='riders',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='BikeControl.ridersprofile'),
        ),
        migrations.AddField(
            model_name='makerequestcash_ph',
            name='riders',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='BikeControl.ridersprofile'),
        ),
        migrations.AlterField(
            model_name='errand_service_ph',
            name='category',
            field=models.CharField(choices=[('Pizza', 'Pizza'), ('Gas', 'Gas'), ('Drugs', 'Drugs'), ('Ice Cream', 'Ice Cream'), ('Bread', 'Bread'), ('Food', 'Food'), ('Others', 'Others'), ('Fuel', 'Fuel'), ('Shawarma', 'Shawarma'), ('Fruits', 'Fruits')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='errand_service_ph',
            name='status',
            field=models.CharField(choices=[('On Route for Delivery', 'On route for Delivery'), ('Pending', 'Pending'), ('Purchase in Process', 'Purchase in Process'), ('Delivered', 'Delivered')], default='Pending', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='makerequestcash_ph',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Canceled', 'Canceled'), ('Delivered', 'Delivered')], default='Pending', max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='Front_desk_PH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, max_length=100, null=True)),
                ('item_description', models.CharField(blank=True, max_length=200, null=True)),
                ('customer_location', models.CharField(blank=True, max_length=100, null=True, verbose_name='Delivery Address')),
                ('delivery_destination', models.CharField(blank=True, max_length=200, null=True, verbose_name='Receiver Location')),
                ('Reciever_phone_number', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')], verbose_name='Reciever Number')),
                ('Receiver_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Customer_phone_number', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')], verbose_name='Customer Phone Number')),
                ('Choice_for_TP', models.CharField(choices=[('Bike', 'Bike'), ('Tricycle', 'Tricycle (Keke)'), ('Van', 'Van')], max_length=100, null=True)),
                ('Delivery_type', models.CharField(choices=[('Pick & Drop', 'Pick & Drop'), ('Errand', 'Errand')], max_length=100, null=True)),
                ('Purchase_location', models.CharField(blank=True, max_length=100, null=True)),
                ('Cancelation_Reason', models.CharField(blank=True, max_length=100, null=True)),
                ('Quantity', models.CharField(blank=True, max_length=100, null=True)),
                ('Enter_amount', models.IntegerField(blank=True, help_text='Cost to purchase items', null=True, verbose_name='Item Amount')),
                ('Note', models.CharField(blank='True', max_length=100, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('order_id', models.CharField(max_length=7, null=True)),
                ('assigned', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Canceled', 'Canceled'), ('Delivered', 'Delivered')], default='Pending', max_length=100, null=True)),
                ('customer_payment_method', models.CharField(choices=[('Transfer & Cash', 'Transfer & Cash'), ('Card', 'Card'), ('Cash', 'Cash'), ('Transfer', 'Transfer')], max_length=100, null=True)),
                ('payments_confirmed', models.BooleanField(default=False)),
                ('paid', models.BooleanField(default=False)),
                ('confirmed', models.BooleanField(default=False)),
                ('profit', models.IntegerField(default=0, null=True)),
                ('Amount_Paid', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('Amount_Payable', models.IntegerField(default=500, null=True)),
                ('Total', models.IntegerField(null=True)),
                ('Delivery_Fee', models.IntegerField(null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.customer')),
                ('riders', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='BikeControl.ridersprofile')),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
    ]
