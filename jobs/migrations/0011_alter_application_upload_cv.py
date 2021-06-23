# Generated by Django 3.2.3 on 2021-06-18 14:12

from django.db import migrations, models
import jobs.validators


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_alter_application_upload_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='upload_cv',
            field=models.FileField(upload_to='uploadcv/', validators=[jobs.validators.validate_file_extension]),
        ),
    ]
