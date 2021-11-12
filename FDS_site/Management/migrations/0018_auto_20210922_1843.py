# Generated by Django 3.1.7 on 2021-09-22 17:43

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0017_auto_20210921_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office_report',
            name='feedback_Manager_FLM',
            field=tinymce.models.HTMLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='feedback_admin',
            field=tinymce.models.HTMLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='feedback_chairman',
            field=tinymce.models.HTMLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='feedback_manager',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='feedback_operations',
            field=tinymce.models.HTMLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='feedback_runyi',
            field=tinymce.models.HTMLField(blank=True, max_length=1000, null=True),
        ),
    ]
