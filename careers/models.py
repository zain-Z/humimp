from django.db import models
from .validators import validate_image_extension
from datetime import date
from django.utils.translation import gettext_lazy as _

JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)


class CareerDetail(models.Model):
    image_career_details = models.FileField(
        validators=[validate_image_extension], upload_to='background/career_details/',  default='',  blank=True)
    title = models.CharField(max_length=300, default='',   blank=True)
    description = models.TextField(default='', blank=True)

    # Roles and Resposibilities
    role_1 = models.TextField(default='', blank=True)
    role_2 = models.TextField(default='', blank=True)
    role_3 = models.TextField(default='', blank=True)
    role_4 = models.TextField(default='', blank=True)
    role_5 = models.TextField(default='', blank=True)
    role_6 = models.TextField(default='', blank=True)
    role_7 = models.TextField(default='', blank=True)
    role_8 = models.TextField(default='', blank=True)
    role_9 = models.TextField(default='', blank=True)
    role_10 = models.TextField(default='', blank=True)
    role_11 = models.TextField(default='', blank=True)
    role_12 = models.TextField(default='', blank=True)
    role_13 = models.TextField(default='', blank=True)
    role_14 = models.TextField(default='', blank=True)
    role_15 = models.TextField(default='', blank=True)
    role_16 = models.TextField(default='', blank=True)
    role_17 = models.TextField(default='', blank=True)
    role_18 = models.TextField(default='', blank=True)
    role_19 = models.TextField(default='', blank=True)
    role_20 = models.TextField(default='', blank=True)

    # Qualifications & Preferred Skills
    skill_1 = models.TextField(default='', blank=True)
    skill_2 = models.TextField(default='', blank=True)
    skill_3 = models.TextField(default='', blank=True)
    skill_4 = models.TextField(default='', blank=True)
    skill_5 = models.TextField(default='', blank=True)
    skill_6 = models.TextField(default='', blank=True)
    skill_7 = models.TextField(default='', blank=True)
    skill_8 = models.TextField(default='', blank=True)
    skill_9 = models.TextField(default='', blank=True)
    skill_10 = models.TextField(default='', blank=True)
    skill_11 = models.TextField(default='', blank=True)
    skill_12 = models.TextField(default='', blank=True)
    skill_13 = models.TextField(default='', blank=True)
    skill_14 = models.TextField(default='', blank=True)
    skill_15 = models.TextField(default='', blank=True)
    skill_16 = models.TextField(default='', blank=True)
    skill_17 = models.TextField(default='', blank=True)
    skill_18 = models.TextField(default='', blank=True)
    skill_19 = models.TextField(default='', blank=True)
    skill_20 = models.TextField(default='', blank=True)
    contract_duration = models.CharField(
        max_length=300, default='',   blank=True)
    governorate = models.CharField(
        max_length=300, default='',   blank=True)
    job_type = models.CharField(
        choices=JOB_TYPE, max_length=1,  default='',  blank=True)
    job_shift = models.CharField(
        choices=JOB_TYPE, max_length=1, default='',   blank=True)
    location = models.CharField(
        max_length=300, default='',   blank=True)
    posted = models.DateField(default=date.today,   blank=True)
    minimum_education = models.CharField(
        max_length=300, default='',   blank=True)
    minimum_experience = models.CharField(
        max_length=300, default='',   blank=True)
    required_travel = models.CharField(
        max_length=150, default='',   blank=True)
    no_of_jobs = models.PositiveIntegerField(default=1,   blank=True)
    deadline = models.DateField(default=date.today,   blank=True)
    puplished = models.DateField(default=date.today,   blank=True)

    def __str__(self):
        return self.title


class CareerList(models.Model):
    image_bg_career_list = models.FileField(
        validators=[validate_image_extension], upload_to='background/career_list/', default='',   blank=True)


class CareerDetatilImage(models.Model):

    image_header_logo_sticky_career_detail_image = models.FileField(
        validators=[validate_image_extension], upload_to='background/career_detail_image/', default='',   blank=True)
    image_footer_logo_career_detail_image = models.FileField(
        validators=[validate_image_extension], upload_to='background/career_detail_image/', default='',   blank=True)
