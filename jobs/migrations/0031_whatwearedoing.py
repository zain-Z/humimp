# Generated by Django 3.2.4 on 2021-06-22 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0030_auto_20210622_0200'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhatWeAreDoing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_layer_bg', models.ImageField(height_field=1920, upload_to='', width_field=350)),
            ],
        ),
    ]
