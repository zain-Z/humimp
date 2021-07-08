# Generated by Django 3.0.6 on 2021-07-08 01:05

import blogs.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20210703_2243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storiesdetail',
            old_name='image_bg_stories_detail',
            new_name='image_stories_detail_five_teaba',
        ),
        migrations.RenameField(
            model_name='storiesdetail',
            old_name='image_footer_logo_stories_detail',
            new_name='image_stories_detail_four_teaba',
        ),
        migrations.RenameField(
            model_name='storiesdetail',
            old_name='image_header_logo_sticky_stories_detail',
            new_name='image_stories_detail_one_teaba',
        ),
        migrations.RenameField(
            model_name='storiesdetail',
            old_name='image_stories_detail_five',
            new_name='image_stories_detail_sex_teaba',
        ),
        migrations.RenameField(
            model_name='storiesdetail',
            old_name='image_stories_detail_four',
            new_name='image_stories_detail_three_teaba',
        ),
        migrations.RenameField(
            model_name='storiesdetail',
            old_name='image_stories_detail_left',
            new_name='image_stories_detail_two_teaba',
        ),
        migrations.RenameField(
            model_name='storiesdetail',
            old_name='image_stories_detail_middle',
            new_name='stories_details_image_one',
        ),
        migrations.RenameField(
            model_name='storiesdetail',
            old_name='image_stories_detail_one',
            new_name='stories_details_image_three',
        ),
        migrations.RenameField(
            model_name='storiesdetail',
            old_name='image_stories_detail_right',
            new_name='stories_details_image_two',
        ),
        migrations.RemoveField(
            model_name='storiesdetail',
            name='image_stories_detail_sex',
        ),
        migrations.RemoveField(
            model_name='storiesdetail',
            name='image_stories_detail_three',
        ),
        migrations.RemoveField(
            model_name='storiesdetail',
            name='image_stories_detail_two',
        ),
        migrations.RemoveField(
            model_name='storiesdetail',
            name='stories_details_image1',
        ),
        migrations.RemoveField(
            model_name='storiesdetail',
            name='stories_details_image2',
        ),
        migrations.RemoveField(
            model_name='storiesdetail',
            name='stories_details_image3',
        ),
        migrations.AlterField(
            model_name='story',
            name='stories_image',
            field=models.FileField(blank=True, null=True, upload_to='background/story/', validators=[blogs.validators.validate_image_extension]),
        ),
        migrations.AlterField(
            model_name='team',
            name='teams_image',
            field=models.FileField(blank=True, null=True, upload_to='background/team/', validators=[blogs.validators.validate_image_extension]),
        ),
    ]
