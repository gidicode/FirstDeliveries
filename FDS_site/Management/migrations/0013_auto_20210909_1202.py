# Generated by Django 3.1.7 on 2021-09-09 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0012_auto_20210909_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office_report',
            name='Fleet_report',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Fleet_report_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='FrontDesk_report',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='FrontDesk_report_Title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Front_desk_total_amount',
            field=models.IntegerField(blank=True, null=True, verbose_name='Total Amount Today'),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Front_desk_total_rides',
            field=models.IntegerField(blank=True, null=True, verbose_name='Total Rides Today'),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Ict_report',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Ict_report_Title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Iwh_report',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Iwh_report_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Manager_report',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Manager_report_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Marketing_report',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Marketing_report_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Runyi_report',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Runyi_report_Title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Tank_farm_report',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='Tank_farm_report_title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Report Title'),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='extent_of_completion',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Task Completed'),
        ),
        migrations.AlterField(
            model_name='office_report',
            name='solutions',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
