from django.db import models
from .validators import validate_image_extension
from datetime import date


JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)


class CareerDetail(models.Model):
    image_career_details = models.FileField(
        validators=[validate_image_extension], upload_to='background/career_details/', null=True, blank=True)
    title = models.CharField(max_length=300, default='', null=True)
    description = models.TextField(null=True)
    contract_duration = models.CharField(max_length=300, default='', )
    governorate = models.CharField(max_length=300, default='')
    job_type = models.CharField(choices=JOB_TYPE, max_length=1)
    job_shift = models.CharField(choices=JOB_TYPE, max_length=1)
    location = models.CharField(max_length=300, default='', null=True)
    posted = models.DateField(default=date.today)
    minimum_education = models.CharField(max_length=300, default='')
    minimum_experience = models.CharField(max_length=300, default='')
    required_travel = models.CharField(max_length=150, default='')
    no_of_jobs = models.PositiveIntegerField(default=1)
    deadline = models.DateField(default=date.today)
    puplished = models.DateField(default=date.today)

    def __str__(self):
        return self.title
