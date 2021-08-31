# Generated by Django 3.1.7 on 2021-08-23 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0132_auto_20210823_2232'),
        ('Management', '0002_auto_20210823_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='management_notification',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.customer'),
        ),
        migrations.AddField(
            model_name='office_report',
            name='submit',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
