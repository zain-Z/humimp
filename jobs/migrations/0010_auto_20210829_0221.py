# Generated by Django 3.0.6 on 2021-08-29 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_auto_20210828_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='arabic',
            field=models.CharField(blank=True, default='Arabic', max_length=6),
        ),
        migrations.AlterField(
            model_name='application',
            name='english',
            field=models.CharField(blank=True, default='English', max_length=7),
        ),
        migrations.AlterField(
            model_name='application',
            name='full_name',
            field=models.CharField(max_length=200, verbose_name='full_name'),
        ),
        migrations.AlterField(
            model_name='application',
            name='kurdish',
            field=models.CharField(blank=True, default='Kurdish', max_length=7),
        ),
    ]
