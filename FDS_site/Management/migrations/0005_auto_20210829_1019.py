# Generated by Django 3.1.7 on 2021-08-29 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0004_auto_20210825_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='office_report',
            name='feedback_manager',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='office_report',
            name='feedback_runyi',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='office_report',
            name='manager_seen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='office_report',
            name='runyi_seen',
            field=models.BooleanField(default=False),
        ),
    ]
