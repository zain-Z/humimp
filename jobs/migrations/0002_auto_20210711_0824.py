# Generated by Django 3.0.6 on 2021-07-11 06:24

from django.db import migrations, models
import jobs.validators


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhatWeAreDoingDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whatDoDetail_image_gallery', models.FileField(blank=True, null=True, upload_to='background/WhatWeAreDoingDetails/', validators=[jobs.validators.validate_image_extension])),
                ('whatDoDetail_image1', models.FileField(blank=True, null=True, upload_to='background/WhatWeAreDoingDetails/', validators=[jobs.validators.validate_image_extension])),
                ('whatDoDetail_image2', models.FileField(blank=True, null=True, upload_to='background/WhatWeAreDoingDetails/', validators=[jobs.validators.validate_image_extension])),
                ('whatDoDetail_image3', models.FileField(blank=True, null=True, upload_to='background/WhatWeAreDoingDetails/', validators=[jobs.validators.validate_image_extension])),
                ('whatDoDetail_name', models.CharField(default='', max_length=300)),
                ('whatDoDetail_desc1', models.CharField(default='', max_length=300)),
                ('whatDoDetail_desc2', models.CharField(default='', max_length=300)),
                ('whatDoDetail_desc3', models.CharField(default='', max_length=300)),
                ('whatDoDetail_desc4', models.CharField(default='', max_length=300)),
                ('whatDoDetail_desc5', models.CharField(default='', max_length=300)),
                ('whatDoDetail_desc6', models.CharField(default='', max_length=300)),
                ('whatDoDetail_desc7', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='WhatWeAreDoing',
        ),
        migrations.DeleteModel(
            name='WhatWeAreDoingDetails',
        ),
    ]