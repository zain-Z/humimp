# Generated by Django 3.0.6 on 2021-08-29 00:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_auto_20210829_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='phone',
            field=models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'.             Up to 14 digits allowed.", regex='^\\+?1?\\d{9,14}$')], verbose_name='phone'),
        ),
    ]
