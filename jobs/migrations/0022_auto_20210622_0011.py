# Generated by Django 3.2.4 on 2021-06-21 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0021_auto_20210622_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='arabic',
            field=models.BooleanField(blank=True, choices=[('Arabic', 'Arabic')], default=True, max_length=6),
        ),
        migrations.AlterField(
            model_name='application',
            name='english',
            field=models.BooleanField(blank=True, choices=[('English', 'English')], default=True, max_length=7),
        ),
        migrations.AlterField(
            model_name='application',
            name='kurdish',
            field=models.BooleanField(blank=True, choices=[('Kurdish', 'Kurdish')], default=True, max_length=7),
        ),
    ]
