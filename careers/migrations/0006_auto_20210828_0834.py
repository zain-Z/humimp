# Generated by Django 3.0.6 on 2021-08-28 06:34

import careers.validators
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0005_auto_20210825_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careerdetail',
            name='contract_duration',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='deadline',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='governorate',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='image_career_details',
            field=models.FileField(blank=True, default='', upload_to='background/career_details/', validators=[careers.validators.validate_image_extension]),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='job_shift',
            field=models.CharField(blank=True, choices=[('1', 'Full time'), ('2', 'Part time'), ('3', 'Internship')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='job_type',
            field=models.CharField(blank=True, choices=[('1', 'Full time'), ('2', 'Part time'), ('3', 'Internship')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='location',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='minimum_education',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='minimum_experience',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='no_of_jobs',
            field=models.PositiveIntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='posted',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='puplished',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='required_travel',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='role_1',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='role_10',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='role_11',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='role_12',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='role_13',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='role_14',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='role_15',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='role_16',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='role_17',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='role_18',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='role_19',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='role_2',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='role_20',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='role_3',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='role_4',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='role_5',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='role_6',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='role_7',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='role_8',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='role_9',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='skill_1',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='skill_10',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='skill_11',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='skill_12',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='skill_13',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='skill_14',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='skill_15',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='skill_16',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='skill_17',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='skill_18',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='skill_19',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='skill_2',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='skill_20',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='skill_3',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='skill_4',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='skill_5',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='skill_6',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='skill_7',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='skill_8',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='skill_9',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='careerdetail',
            name='title',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='careerdetatilimage',
            name='image_footer_logo_career_detail_image',
            field=models.FileField(blank=True, default='', upload_to='background/career_detail_image/', validators=[careers.validators.validate_image_extension]),
        ),
        migrations.AlterField(
            model_name='careerdetatilimage',
            name='image_header_logo_sticky_career_detail_image',
            field=models.FileField(blank=True, default='', upload_to='background/career_detail_image/', validators=[careers.validators.validate_image_extension]),
        ),
        migrations.AlterField(
            model_name='careerlist',
            name='image_bg_career_list',
            field=models.FileField(blank=True, default='', upload_to='background/career_list/', validators=[careers.validators.validate_image_extension]),
        ),
    ]