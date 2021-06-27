from django.db import models
from ckeditor.fields import RichTextField
from .validators import validate_image_extension

JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)


class CareerDetail(models.Model):

    image_bg_career = models.FileField(
        validators=[validate_image_extension], upload_to='background/career/', null=True, blank=True)
    title = models.CharField(max_length=300, default='')
    description = RichTextField()
    contract_duration = models.CharField(max_length=300, default='')
    job_type = models.CharField(choices=JOB_TYPE, max_length=1)
    job_shift = models.CharField(choices=JOB_TYPE, max_length=1)
    location = models.CharField(max_length=300, default='')
    posted = models.DateTimeField(auto_now=True)
    minimum_education = models.CharField(max_length=300, default='')
    minimum_experience = models.CharField(max_length=300, default='')
    required_travel = models.CharField(max_length=150, default='')
    no_of_jobs = models.PositiveIntegerField(default=1)
    deadline = models.DateTimeField(auto_now=False)
    image_footer_logo_career_detail = models.FileField(
        validators=[validate_image_extension], upload_to='background/career/', null=True, blank=True)
    image_header_logo_sticky_career_detail = models.FileField(
        validators=[validate_image_extension], upload_to='background/career/', null=True, blank=True)

    def __str__(self):
        return self.title
