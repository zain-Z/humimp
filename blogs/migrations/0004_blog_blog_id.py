# Generated by Django 3.0.6 on 2021-08-23 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20210814_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_id',
            field=models.IntegerField(default=1),
        ),
    ]