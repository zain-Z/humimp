# Generated by Django 3.0.6 on 2021-08-28 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_auto_20210828_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='full_name',
            field=models.CharField(help_text='this is the help text', max_length=200, verbose_name='full_name'),
        ),
    ]