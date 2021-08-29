# Generated by Django 3.0.6 on 2021-08-25 13:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0004_auto_20210824_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careerdetail',
            name='contract_duration',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='deadline',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='governorate',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='job_shift',
            field=models.CharField(blank=True, choices=[('1', 'Full time'), ('2', 'Part time'), ('3', 'Internship')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='job_type',
            field=models.CharField(blank=True, choices=[('1', 'Full time'), ('2', 'Part time'), ('3', 'Internship')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='location',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='minimum_education',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='minimum_experience',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='no_of_jobs',
            field=models.PositiveIntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='posted',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='puplished',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='required_travel',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='title',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
    ]