# Generated by Django 3.1.7 on 2021-06-29 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0093_auto_20210629_1647'),
        ('BikeControl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ridersdeliveries',
            name='errand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.errand_service'),
        ),
        migrations.AddField(
            model_name='ridersdeliveries',
            name='front_desk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.front_desk'),
        ),
    ]
