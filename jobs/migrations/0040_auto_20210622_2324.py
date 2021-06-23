# Generated by Django 3.2.4 on 2021-06-22 21:24

from django.db import migrations, models
import jobs.validators


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0039_auto_20210622_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='image_index_stories_four',
            field=models.FileField(blank=True, null=True, upload_to='background/', validators=[jobs.validators.validate_image_extension]),
        ),
        migrations.AddField(
            model_name='index',
            name='image_index_stories_three',
            field=models.FileField(blank=True, null=True, upload_to='background/', validators=[jobs.validators.validate_image_extension]),
        ),
        migrations.AddField(
            model_name='index',
            name='image_index_stories_two',
            field=models.FileField(blank=True, null=True, upload_to='background/', validators=[jobs.validators.validate_image_extension]),
        ),
    ]
