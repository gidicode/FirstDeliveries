# Generated by Django 3.1.7 on 2021-09-15 13:03

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0013_auto_20210909_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office_report',
            name='Fleet_challenges',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Fleet_report',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Fleet_solutions',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='FrontDesk_challenges',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='FrontDesk_report',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='FrontDesk_solutions',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Ict_challenges',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Ict_report',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Ict_solutions',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Iwh_challenges',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Challenges'),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Iwh_report',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Iwh_solutions',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Solutions'),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Manager_challenges',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Manager_report',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Manager_solutions',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Marketing_report',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Marketing_solutions',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Marketting_challenges',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Runyi_challenges',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Runyi_report',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Runyi_solutions',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Tank_farm_challenges',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Challenges'),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Tank_farm_report',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Tank_farm_solutions',
            field=models.CharField(blank=True, max_length=5000, null=True, verbose_name='Solutions'),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Work_description',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Main Report'),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='challenges',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='extent_of_completion',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Task Completed'),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='feedback_Manager_FLM',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='feedback_admin',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='feedback_chairman',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='feedback_manager',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='feedback_operations',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='feedback_runyi',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='solutions',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='time_taken',
            field=models.TextField(choices=[(None, None), ('0-1HR', '0-1HR'), ('1-2HRS', '1-2HRS'), ('2-3HRS', '2-3HRS'), ('3-4HRS', '3-4HRS'), ('4-5HRS', '4-5HRS')], max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='work_left',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Task Left'),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='work_schedule',
            field=tinymce.models.HTMLField(blank=True, max_length=5000, null=True, verbose_name='Task Schedule'),
        ),
    ]
