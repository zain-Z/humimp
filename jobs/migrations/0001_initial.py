# Generated by Django 3.2.4 on 2021-06-27 04:51

import django.core.validators
from django.db import migrations, models
import jobs.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_bg_about', models.FileField(blank=True, null=True, upload_to='background/about/', validators=[jobs.validators.validate_image_extension])),
                ('image_middle_about', models.FileField(blank=True, null=True, upload_to='background/about/', validators=[jobs.validators.validate_image_extension])),
                ('image_header_logo_sticky_about', models.FileField(blank=True, null=True, upload_to='background/about/', validators=[jobs.validators.validate_image_extension])),
                ('image_footer_logo_about', models.FileField(blank=True, null=True, upload_to='background/about/', validators=[jobs.validators.validate_image_extension])),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True)),
                ('phone', models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'.             Up to 14 digits allowed.", regex='^\\+?1?\\d{9,14}$')])),
                ('region', models.CharField(choices=[('Baghdad', 'Baghdad'), ('Mousl', 'Mousl'), ('Erbil', 'Erbil'), ('Anbar', 'Anbar'), ('Babylon', 'Babylon'), ('Basra', 'Basra'), ('Dhi Qar', 'Dhi Qar'), ('Diyala', 'Diyala'), ('Dohuk', 'Dohuk'), ('Karbala', 'Karbala'), ('KirKuk', 'KirKuk'), ('Maysan', 'Maysan'), ('Najaf', 'Najaf'), ('Qaisiyah', 'Qaisiyah'), ('Salahaddin', 'Salahaddin'), ('Sulaymaniyah', 'Sulaymaniyah'), ('Wasit', 'Wasit')], max_length=12)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=6)),
                ('english', models.CharField(blank=True, default='English', max_length=7, null=True)),
                ('kurdish', models.CharField(blank=True, default='Kurdish', max_length=7, null=True)),
                ('arabic', models.CharField(blank=True, default='Arabic', max_length=6, null=True)),
                ('cover_letter', models.TextField()),
                ('upload_cv', models.FileField(upload_to='uploadcv/', validators=[jobs.validators.validate_file_extension])),
            ],
        ),
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_bg_donate', models.FileField(blank=True, null=True, upload_to='background/donate/', validators=[jobs.validators.validate_image_extension])),
                ('image_header_logo_sticky_donate', models.FileField(blank=True, null=True, upload_to='background/donate/', validators=[jobs.validators.validate_image_extension])),
                ('image_footer_logo_donate', models.FileField(blank=True, null=True, upload_to='background/donate/', validators=[jobs.validators.validate_image_extension])),
            ],
        ),
        migrations.CreateModel(
            name='GetInvolved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_bg_getinvolved', models.FileField(blank=True, null=True, upload_to='background/about/', validators=[jobs.validators.validate_image_extension])),
                ('image_careers_getinvolved', models.FileField(blank=True, null=True, upload_to='background/about/', validators=[jobs.validators.validate_image_extension])),
                ('image_joinus_getinvolved', models.FileField(blank=True, null=True, upload_to='background/about/', validators=[jobs.validators.validate_image_extension])),
                ('image_header_logo_sticky_getinvolved', models.FileField(blank=True, null=True, upload_to='background/about/', validators=[jobs.validators.validate_image_extension])),
                ('image_footer_logo_getinvolved', models.FileField(blank=True, null=True, upload_to='background/about/', validators=[jobs.validators.validate_image_extension])),
            ],
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_bg_index_one', models.FileField(blank=True, null=True, upload_to='background/index/', validators=[jobs.validators.validate_image_extension])),
                ('image_bg_index_two', models.FileField(blank=True, null=True, upload_to='background/index/', validators=[jobs.validators.validate_image_extension])),
                ('image_bg_index_three', models.FileField(blank=True, null=True, upload_to='background/index/', validators=[jobs.validators.validate_image_extension])),
                ('index_animals', models.FileField(blank=True, null=True, upload_to='background/index/', validators=[jobs.validators.validate_image_extension])),
                ('image_index_stories_one', models.FileField(blank=True, null=True, upload_to='background/index/', validators=[jobs.validators.validate_image_extension])),
                ('image_index_stories_two', models.FileField(blank=True, null=True, upload_to='background/index/', validators=[jobs.validators.validate_image_extension])),
                ('image_index_stories_three', models.FileField(blank=True, null=True, upload_to='background/index/', validators=[jobs.validators.validate_image_extension])),
                ('image_index_stories_four', models.FileField(blank=True, null=True, upload_to='background/index/', validators=[jobs.validators.validate_image_extension])),
                ('image_footer_logo', models.FileField(blank=True, null=True, upload_to='background/index/', validators=[jobs.validators.validate_image_extension])),
                ('image_header_logo_sticky', models.FileField(blank=True, null=True, upload_to='background/index/', validators=[jobs.validators.validate_image_extension])),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_bg_volunteer', models.FileField(blank=True, null=True, upload_to='background/volunteer/', validators=[jobs.validators.validate_image_extension])),
                ('image_header_logo_sticky_volunteer', models.FileField(blank=True, null=True, upload_to='background/volunteer/', validators=[jobs.validators.validate_image_extension])),
                ('image_footer_logo_volunteer', models.FileField(blank=True, null=True, upload_to='background/volunteer/', validators=[jobs.validators.validate_image_extension])),
            ],
        ),
        migrations.CreateModel(
            name='WhatWeAreDoing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_bg_what_we_are_doing', models.FileField(blank=True, null=True, upload_to='background/whatwe/', validators=[jobs.validators.validate_image_extension])),
                ('image_header_logo_sticky_what_we_are_doing', models.FileField(blank=True, null=True, upload_to='background/whatwe/', validators=[jobs.validators.validate_image_extension])),
                ('image_footer_logo_what_we_are_doing', models.FileField(blank=True, null=True, upload_to='background/whatwe/', validators=[jobs.validators.validate_image_extension])),
            ],
        ),
        migrations.CreateModel(
            name='WhatWeAreDoingDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_bg_what_we_are_doing_details', models.FileField(blank=True, null=True, upload_to='background/WhatWeDetails/', validators=[jobs.validators.validate_image_extension])),
                ('image_what_we_are_doing_details_right', models.FileField(blank=True, null=True, upload_to='background/WhatWeDetails/', validators=[jobs.validators.validate_image_extension])),
                ('image_what_we_are_doing_details_middle', models.FileField(blank=True, null=True, upload_to='background/WhatWeDetails/', validators=[jobs.validators.validate_image_extension])),
                ('image_what_we_are_doing_details_left', models.FileField(blank=True, null=True, upload_to='background/WhatWeDetails/', validators=[jobs.validators.validate_image_extension])),
                ('image_what_we_are_doing_details_one', models.FileField(blank=True, null=True, upload_to='background/WhatWeDetails/', validators=[jobs.validators.validate_image_extension])),
                ('image_what_we_are_doing_details_two', models.FileField(blank=True, null=True, upload_to='background/WhatWeDetails/', validators=[jobs.validators.validate_image_extension])),
                ('image_what_we_are_doing_details_three', models.FileField(blank=True, null=True, upload_to='background/WhatWeDetails/', validators=[jobs.validators.validate_image_extension])),
                ('image_what_we_are_doing_details_four', models.FileField(blank=True, null=True, upload_to='background/WhatWeDetails/', validators=[jobs.validators.validate_image_extension])),
                ('image_what_we_are_doing_details_five', models.FileField(blank=True, null=True, upload_to='background/WhatWeDetails/', validators=[jobs.validators.validate_image_extension])),
                ('image_what_we_are_doing_details_sex', models.FileField(blank=True, null=True, upload_to='background/WhatWeDetails/', validators=[jobs.validators.validate_image_extension])),
                ('image_footer_logo_what_we_are_doing_details', models.FileField(blank=True, null=True, upload_to='background/WhatWeDetails/', validators=[jobs.validators.validate_image_extension])),
                ('image_header_logo_sticky_what_we_are_doing_details', models.FileField(blank=True, null=True, upload_to='background/WhatWeDetails/', validators=[jobs.validators.validate_image_extension])),
            ],
        ),
        migrations.CreateModel(
            name='WhoWeAre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_bg_who_we_are', models.FileField(blank=True, null=True, upload_to='background/about/', validators=[jobs.validators.validate_image_extension])),
                ('image_left_who_we_are', models.FileField(blank=True, null=True, upload_to='background/about/', validators=[jobs.validators.validate_image_extension])),
                ('image_middle_who_we_are', models.FileField(blank=True, null=True, upload_to='background/about/', validators=[jobs.validators.validate_image_extension])),
                ('image_right_who_we_are', models.FileField(blank=True, null=True, upload_to='background/about/', validators=[jobs.validators.validate_image_extension])),
                ('image_header_logo_sticky_who_we_are', models.FileField(blank=True, null=True, upload_to='background/about/', validators=[jobs.validators.validate_image_extension])),
                ('image_footer_logo_who_we_are', models.FileField(blank=True, null=True, upload_to='background/about/', validators=[jobs.validators.validate_image_extension])),
            ],
        ),
    ]
