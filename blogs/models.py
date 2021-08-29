from django.db import models
from .validators import validate_image_extension
from django.utils.translation import gettext_lazy as _

from datetime import date


class Blog(models.Model):

    blogs_image = models.FileField(
        validators=[validate_image_extension], upload_to='background/blogs/', default='', blank=True)

    blogs_date = models.DateField(default=date.today, blank=True)
    blogs_desc = models.CharField(
        max_length=300, default='',   blank=True)
    blogs_location = models.CharField(
        max_length=300, default='',   blank=True)


class Team(models.Model):
    teams_image = models.FileField(
        validators=[validate_image_extension], upload_to='background/team/',  default='',  blank=True)
    teams_name = models.CharField(
        max_length=300, default='',   blank=True)

    teams_desc = models.CharField(
        max_length=300, default='',   blank=True)


class StoryDetail(models.Model):

    story_image_one = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_detail/', default='',   blank=True)
    story_image_two = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_detail/', default='',   blank=True)
    story_image_three = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_detail/', default='',   blank=True)

    story_date = models.DateField(default=date.today,   blank=True)
    story_location = models.CharField(
        max_length=300, default='',   blank=True)
    story_name = models.CharField(
        max_length=300, default='',   blank=True)
    story_desc1 = models.CharField(
        max_length=300, default='',   blank=True)
    story_desc2 = models.CharField(
        max_length=300, default='',   blank=True)
    story_desc3 = models.CharField(
        max_length=300, default='',   blank=True)
    story_desc4 = models.CharField(
        max_length=300, default='',   blank=True)
    story_desc5 = models.CharField(
        max_length=300, default='',   blank=True)
    story_desc6 = models.CharField(
        max_length=300, default='',   blank=True)
    story_desc7 = models.CharField(
        max_length=300, default='',   blank=True)

    class Meta:
        ordering = ['-story_date']


class StoryAndBlog(models.Model):
    image_bg_stories = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_and_blogs/', default='',   blank=True)
    text_bg_stories = models.CharField(
        max_length=300, default='',   blank=True)

    image_bg_blogs = models.FileField(
        validators=[validate_image_extension], upload_to='background/stories_and_blogs/',  default='',  blank=True)
    text_bg_blogs = models.CharField(
        max_length=300, default='',   blank=True)
