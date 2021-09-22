# Generated by Django 3.1.7 on 2021-09-21 13:22

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0016_auto_20210920_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office_report',
            name='Categoty',
            field=models.CharField(choices=[('Operations', 'Operations'), ('Fleet', 'Fleet'), ('ICT', 'ICT'), ('Front', 'Front'), ('Market', 'Market'), ('Tank Farm', 'Tank Farm'), ('IWH', 'IWH'), ('RUNYI', 'RUNYI'), ('MANAGER', 'MANAGER'), ('COMMERCIAL', 'COMMERCIAL')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='feedback_runyi',
            field=tinymce.models.HTMLField(max_length=1000, null=True),
        ),
    ]
