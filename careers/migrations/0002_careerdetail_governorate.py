# Generated by Django 3.2.4 on 2021-06-27 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='careerdetail',
            name='governorate',
            field=models.CharField(default='', max_length=300),
        ),
    ]
