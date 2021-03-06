# Generated by Django 3.0.6 on 2021-07-11 04:51

import careers.validators
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CareerDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_career_details', models.FileField(blank=True, null=True, upload_to='background/career_details/', validators=[careers.validators.validate_image_extension])),
                ('title', models.CharField(default='', max_length=300, null=True)),
                ('description', models.TextField(null=True)),
                ('contract_duration', models.CharField(default='', max_length=300)),
                ('governorate', models.CharField(default='', max_length=300)),
                ('job_type', models.CharField(choices=[('1', 'Full time'), ('2', 'Part time'), ('3', 'Internship')], max_length=1)),
                ('job_shift', models.CharField(choices=[('1', 'Full time'), ('2', 'Part time'), ('3', 'Internship')], max_length=1)),
                ('location', models.CharField(default='', max_length=300, null=True)),
                ('posted', models.DateField(default=datetime.date.today)),
                ('minimum_education', models.CharField(default='', max_length=300)),
                ('minimum_experience', models.CharField(default='', max_length=300)),
                ('required_travel', models.CharField(default='', max_length=150)),
                ('no_of_jobs', models.PositiveIntegerField(default=1)),
                ('deadline', models.DateField(default=datetime.date.today)),
                ('puplished', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='CareerDetatilImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_header_logo_sticky_career_detail_image', models.FileField(blank=True, null=True, upload_to='background/career_detail_image/', validators=[careers.validators.validate_image_extension])),
                ('image_footer_logo_career_detail_image', models.FileField(blank=True, null=True, upload_to='background/career_detail_image/', validators=[careers.validators.validate_image_extension])),
            ],
        ),
        migrations.CreateModel(
            name='CareerList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_bg_career_list', models.FileField(blank=True, null=True, upload_to='background/career_list/', validators=[careers.validators.validate_image_extension])),
            ],
        ),
    ]
