# Generated by Django 3.0.6 on 2021-07-11 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20210711_0824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='index',
            name='image_story_index',
        ),
        migrations.RemoveField(
            model_name='index',
            name='text_story_index',
        ),
        migrations.RemoveField(
            model_name='index',
            name='text_what_we_are_doing_index',
        ),
    ]