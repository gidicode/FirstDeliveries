# Generated by Django 3.1.7 on 2021-06-10 10:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0070_auto_20210609_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='makerequest',
            name='reciever_name2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Reciever Name (2)'),
        ),
        migrations.AddField(
            model_name='makerequest',
            name='reciever_name3',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Reciever Name (3)'),
        ),
        migrations.AddField(
            model_name='makerequest',
            name='reciever_name4',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Reciever Name (4)'),
        ),
        migrations.AddField(
            model_name='makerequest',
            name='reciever_name5',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Reciever Name (5)'),
        ),
        migrations.AlterField(
            model_name='anonymous',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Canceled', 'Canceled'), ('Pending', 'Pending'), ('Delivered', 'Delivered')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='makerequest',
            name='reciever_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Reciever Name'),
        ),
        migrations.AlterField(
            model_name='makerequest',
            name='reciever_phone_number',
            field=models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')], verbose_name='Reciever Name (2)'),
        ),
        migrations.AlterField(
            model_name='makerequest',
            name='status',
            field=models.CharField(choices=[('Out for delivery', 'Out for delivery'), ('Canceled', 'Canceled'), ('Pending', 'Pending'), ('Delivered', 'Delivered')], default='Pending', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='Address_of_reciever',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Reciever Address'),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='Address_of_reciever2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Reciever Address (2)'),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='Address_of_reciever3',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Reciever Address (3)'),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='Address_of_reciever4',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Reciever Address (4)'),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='Address_of_reciever5',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Reciever Address (5)'),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='Package_description2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Package Description (2)'),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='Package_description3',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Package Description (3)'),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='Package_description4',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Package Description (4)'),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='Package_description5',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Package Description (5)'),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='reciever_name2',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Reciever Name (2)'),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='reciever_name3',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Reciever Name (3)'),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='reciever_name4',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Reciever Name (4)'),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='reciever_name5',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Reciever Name (5)'),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='reciever_phone_number',
            field=models.CharField(blank=True, help_text='This Format:070xxxxxxxx', max_length=17, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')], verbose_name='Reciever Number'),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='reciever_phone_number2',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')], verbose_name='Reciever Number(2)'),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='reciever_phone_number3',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')], verbose_name='Reciever Number(3)'),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='reciever_phone_number4',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')], verbose_name='Reciever Number(4)'),
        ),
        migrations.AlterField(
            model_name='makerequestcash',
            name='reciever_phone_number5',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')], verbose_name='Reciever Number(5)'),
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
