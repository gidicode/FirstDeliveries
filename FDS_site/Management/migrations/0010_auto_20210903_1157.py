# Generated by Django 3.1.7 on 2021-09-03 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0009_auto_20210902_1120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='office_report',
            old_name='for_admin_operation_runyi',
            new_name='for_admin',
        ),
        migrations.AddField(
            model_name='office_report',
            name='for_manager_FLM',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='office_report',
            name='for_operation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='office_report',
            name='for_runyi',
            field=models.BooleanField(default=False),
        ),
    ]
