# Generated by Django 3.0.6 on 2021-08-23 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_blog_blog_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='blog_id',
        ),
    ]