# Generated by Django 3.0.6 on 2021-07-11 04:51

import blogs.validators
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogs_image', models.FileField(blank=True, null=True, upload_to='background/blogs/', validators=[blogs.validators.validate_image_extension])),
                ('blogs_date', models.DateField(default=datetime.date.today)),
                ('blogs_desc', models.CharField(default='', max_length=300)),
                ('blogs_location', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='StoriesDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stories_details_image_one', models.FileField(blank=True, null=True, upload_to='background/stories_detail/', validators=[blogs.validators.validate_image_extension])),
                ('stories_details_image_two', models.FileField(blank=True, null=True, upload_to='background/stories_detail/', validators=[blogs.validators.validate_image_extension])),
                ('stories_details_image_three', models.FileField(blank=True, null=True, upload_to='background/stories_detail/', validators=[blogs.validators.validate_image_extension])),
                ('stories_details_date', models.DateField(default=datetime.date.today)),
                ('stories_details_location', models.CharField(default='', max_length=300)),
                ('stories_details_name', models.CharField(default='', max_length=300)),
                ('stories_details_desc1', models.CharField(default='', max_length=300)),
                ('stories_details_desc2', models.CharField(default='', max_length=300)),
                ('stories_details_desc3', models.CharField(default='', max_length=300)),
                ('stories_details_desc4', models.CharField(default='', max_length=300)),
                ('stories_details_desc5', models.CharField(default='', max_length=300)),
                ('stories_details_desc6', models.CharField(default='', max_length=300)),
                ('stories_details_desc7', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='StoryAndBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_bg_stories', models.FileField(blank=True, null=True, upload_to='background/stories_and_blogs/', validators=[blogs.validators.validate_image_extension])),
                ('text_bg_stories', models.CharField(default='', max_length=300)),
                ('image_bg_blogs', models.FileField(blank=True, null=True, upload_to='background/stories_and_blogs/', validators=[blogs.validators.validate_image_extension])),
                ('text_bg_blogs', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='StoryList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stories_image', models.FileField(blank=True, null=True, upload_to='background/story/', validators=[blogs.validators.validate_image_extension])),
                ('stories_date', models.DateField(default=datetime.date.today)),
                ('stories_location', models.CharField(default='', max_length=300)),
                ('stories_name', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teams_image', models.FileField(blank=True, null=True, upload_to='background/team/', validators=[blogs.validators.validate_image_extension])),
                ('teams_name', models.CharField(default='', max_length=300)),
                ('teams_desc', models.CharField(default='', max_length=300)),
            ],
        ),
    ]
