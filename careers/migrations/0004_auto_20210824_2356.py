# Generated by Django 3.0.6 on 2021-08-24 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0003_auto_20210824_2341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='careerdetail',
            name='qualifications_and_preferred_skills',
        ),
        migrations.AddField(
            model_name='careerdetail',
            name='skill_1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='careerdetail',
            name='skill_10',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='careerdetail',
            name='skill_11',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='careerdetail',
            name='skill_12',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='careerdetail',
            name='skill_13',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='careerdetail',
            name='skill_14',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='careerdetail',
            name='skill_15',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='careerdetail',
            name='skill_16',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='careerdetail',
            name='skill_17',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='careerdetail',
            name='skill_18',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='careerdetail',
            name='skill_19',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='careerdetail',
            name='skill_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='careerdetail',
            name='skill_20',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='careerdetail',
            name='skill_3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='careerdetail',
            name='skill_4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='careerdetail',
            name='skill_5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='careerdetail',
            name='skill_6',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='careerdetail',
            name='skill_7',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='careerdetail',
            name='skill_8',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='careerdetail',
            name='skill_9',
            field=models.TextField(blank=True, null=True),
        ),
    ]