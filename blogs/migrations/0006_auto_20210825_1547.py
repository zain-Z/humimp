# Generated by Django 3.0.6 on 2021-08-25 13:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_remove_blog_blog_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blogs_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blogs_desc',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blogs_location',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='storyandblog',
            name='text_bg_blogs',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='storyandblog',
            name='text_bg_stories',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='storydetail',
            name='story_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='storydetail',
            name='story_desc1',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='storydetail',
            name='story_desc2',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='storydetail',
            name='story_desc3',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='storydetail',
            name='story_desc4',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='storydetail',
            name='story_desc5',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='storydetail',
            name='story_desc6',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='storydetail',
            name='story_desc7',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='storydetail',
            name='story_location',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='storydetail',
            name='story_name',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='teams_desc',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='teams_name',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
    ]
