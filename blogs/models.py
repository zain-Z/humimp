from django.db import models
from .validators import validate_image_extension
from django.utils.translation import gettext_lazy as _

from datetime import date


class Blog(models.Model):
    blogs_image = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/', null=True, blank=True)

    blogs_date = models.DateField(default=date.today)
    blogs_desc = models.CharField(max_length=300, default='')
    blogs_location = models.CharField(max_length=300, default='')


class Team(models.Model):
    teams_image = models.FileField(
        validators=[validate_image_extension], upload_to='background/team/', null=True, blank=True)
    teams_name = models.CharField(max_length=300, default='')

    teams_desc = models.CharField(max_length=300, default='')


class StoryDetail(models.Model):

    story_image_one = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_detail/', null=True, blank=True)
    story_image_two = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_detail/', null=True, blank=True)
    story_image_three = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_detail/', null=True, blank=True)

    story_date = models.DateField(default=date.today)
    story_location = models.CharField(max_length=300, default='')
    story_name = models.CharField(max_length=300, default='')
    story_desc1 = models.CharField(max_length=300, default='')
    story_desc2 = models.CharField(max_length=300, default='')
    story_desc3 = models.CharField(max_length=300, default='')
    story_desc4 = models.CharField(max_length=300, default='')
    story_desc5 = models.CharField(max_length=300, default='')
    story_desc6 = models.CharField(max_length=300, default='')
    story_desc7 = models.CharField(max_length=300, default='')


class StoryAndBlog(models.Model):
    image_bg_stories = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_and_blogs/', null=True, blank=True)
    text_bg_stories = models.CharField(max_length=300, default='')

    image_bg_blogs = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_and_blogs/', null=True, blank=True)
    text_bg_blogs = models.CharField(max_length=300, default='')
