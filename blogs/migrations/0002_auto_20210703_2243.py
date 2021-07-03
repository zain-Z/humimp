# Generated by Django 3.0.6 on 2021-07-03 20:43

import blogs.validators
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='image_bg_blogs',
            new_name='blogs_image',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image_blogs_eight',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image_blogs_five',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image_blogs_four',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image_blogs_left',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image_blogs_middle',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image_blogs_one',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image_blogs_right',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image_blogs_seven',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image_blogs_sex',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image_blogs_three',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image_blogs_two',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image_footer_logo_blogs',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image_header_logo_sticky_blogs',
        ),
        migrations.RemoveField(
            model_name='story',
            name='image_bg_story',
        ),
        migrations.RemoveField(
            model_name='story',
            name='image_footer_logo_story',
        ),
        migrations.RemoveField(
            model_name='story',
            name='image_header_logo_sticky_story',
        ),
        migrations.RemoveField(
            model_name='story',
            name='image_story_eight',
        ),
        migrations.RemoveField(
            model_name='story',
            name='image_story_five',
        ),
        migrations.RemoveField(
            model_name='story',
            name='image_story_four',
        ),
        migrations.RemoveField(
            model_name='story',
            name='image_story_one',
        ),
        migrations.RemoveField(
            model_name='story',
            name='image_story_seven',
        ),
        migrations.RemoveField(
            model_name='story',
            name='image_story_sex',
        ),
        migrations.RemoveField(
            model_name='story',
            name='image_story_three',
        ),
        migrations.RemoveField(
            model_name='story',
            name='image_story_two',
        ),
        migrations.RemoveField(
            model_name='team',
            name='image_bg_team',
        ),
        migrations.RemoveField(
            model_name='team',
            name='image_footer_logo_team',
        ),
        migrations.RemoveField(
            model_name='team',
            name='image_header_logo_sticky_team',
        ),
        migrations.RemoveField(
            model_name='team',
            name='image_team_left',
        ),
        migrations.RemoveField(
            model_name='team',
            name='image_team_middle',
        ),
        migrations.RemoveField(
            model_name='team',
            name='image_team_right',
        ),
        migrations.AddField(
            model_name='blog',
            name='blogs_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='blog',
            name='blogs_desc',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='blog',
            name='blogs_location',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='storiesdetail',
            name='stories_details_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='storiesdetail',
            name='stories_details_desc1',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='storiesdetail',
            name='stories_details_desc2',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='storiesdetail',
            name='stories_details_desc3',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='storiesdetail',
            name='stories_details_desc4',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='storiesdetail',
            name='stories_details_desc5',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='storiesdetail',
            name='stories_details_desc6',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='storiesdetail',
            name='stories_details_desc7',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='storiesdetail',
            name='stories_details_image1',
            field=models.FileField(blank=True, null=True, upload_to='background/blogs/', validators=[blogs.validators.validate_image_extension]),
        ),
        migrations.AddField(
            model_name='storiesdetail',
            name='stories_details_image2',
            field=models.FileField(blank=True, null=True, upload_to='background/blogs/', validators=[blogs.validators.validate_image_extension]),
        ),
        migrations.AddField(
            model_name='storiesdetail',
            name='stories_details_image3',
            field=models.FileField(blank=True, null=True, upload_to='background/blogs/', validators=[blogs.validators.validate_image_extension]),
        ),
        migrations.AddField(
            model_name='storiesdetail',
            name='stories_details_location',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='storiesdetail',
            name='stories_details_name',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='story',
            name='stories_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='story',
            name='stories_image',
            field=models.FileField(blank=True, null=True, upload_to='background/blogs/', validators=[blogs.validators.validate_image_extension]),
        ),
        migrations.AddField(
            model_name='story',
            name='stories_location',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='story',
            name='stories_name',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='team',
            name='teams_desc',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='team',
            name='teams_image',
            field=models.FileField(blank=True, null=True, upload_to='background/blogs/', validators=[blogs.validators.validate_image_extension]),
        ),
        migrations.AddField(
            model_name='team',
            name='teams_name',
            field=models.CharField(default='', max_length=300),
        ),
    ]