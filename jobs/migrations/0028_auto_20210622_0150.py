# Generated by Django 3.2.4 on 2021-06-21 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0027_auto_20210622_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='arabic',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='application',
            name='english',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='application',
            name='kurdish',
            field=models.BooleanField(default=False),
        ),
    ]
